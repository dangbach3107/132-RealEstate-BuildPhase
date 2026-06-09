from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd

app = FastAPI(title="Real Estate Valuation API (MVP)")

# Define request schema
class PropertyInput(BaseModel):
    area_m2: float
    num_floors: int
    num_bedrooms: int
    district: str

# Global variables for model and encoder
model = None
encoder = None

@app.on_event("startup")
def load_models():
    global model, encoder
    ml_dir = os.path.join(os.path.dirname(__file__), '../ml')
    model_path = os.path.join(ml_dir, 'model.pkl')
    encoder_path = os.path.join(ml_dir, 'encoder.pkl')
    
    if os.path.exists(model_path) and os.path.exists(encoder_path):
        model = joblib.load(model_path)
        encoder = joblib.load(encoder_path)
        print("Models loaded successfully.")
    else:
        print("Warning: model.pkl or encoder.pkl not found. Please train the model first.")

@app.get("/")
def read_root():
    return {"message": "Welcome to Real Estate Valuation API (MVP Phase)"}

@app.post("/predict")
def predict_price(prop: PropertyInput):
    if model is None or encoder is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Run the training script first.")
        
    try:
        # Encode district
        if prop.district in encoder.classes_:
            encoded_district = encoder.transform([prop.district])[0]
        else:
            # Fallback for unseen district: just use the first one (0) or handle differently
            encoded_district = 0 
            
        # Prepare input array (Must match training order: area_m2, num_floors, num_bedrooms, district_encoded)
        X = pd.DataFrame([{
            'area_m2': prop.area_m2,
            'num_floors': prop.num_floors,
            'num_bedrooms': prop.num_bedrooms,
            'district_encoded': encoded_district
        }])
        
        # Predict
        price_bn = model.predict(X)[0]
        
        # Round to 2 decimal places
        price_bn_rounded = round(float(price_bn), 2)
        
        return {
            "status": "success",
            "input": prop.dict(),
            "predicted_price_bn": price_bn_rounded,
            "message": f"Căn hộ được định giá khoảng {price_bn_rounded} Tỷ VNĐ"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
