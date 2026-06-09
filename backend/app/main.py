from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Real Estate Valuation API (MVP)")

class PropertyInput(BaseModel):
    area_m2: float
    num_floors: int
    num_bedrooms: int
    phan_khu: str
    view: str
    furniture: str

model = None
encoders = None
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "dummy_key"))

@app.on_event("startup")
def load_models():
    global model, encoders
    ml_dir = os.path.join(os.path.dirname(__file__), '../ml')
    model_path = os.path.join(ml_dir, 'model.pkl')
    encoder_path = os.path.join(ml_dir, 'encoder.pkl')
    
    if os.path.exists(model_path) and os.path.exists(encoder_path):
        model = joblib.load(model_path)
        encoders = joblib.load(encoder_path)
        print("Models loaded successfully.")
    else:
        print("Warning: model.pkl or encoder.pkl not found. Please train the model first.")

@app.get("/")
def read_root():
    return {"message": "Welcome to Real Estate Valuation API (MVP Phase)"}

def generate_explanation(prop: PropertyInput, price_bn: float) -> str:
    # Fallback if no valid API key
    if client.api_key == "dummy_key" or not client.api_key:
        return f"(Mock) Căn hộ {prop.area_m2}m2 tại {prop.phan_khu} có mức giá {price_bn} tỷ. Mức giá này phản ánh đúng giá trị thực tế do sở hữu tầm view {prop.view} và tình trạng bàn giao {prop.furniture}."
        
    try:
        prompt = f"""
        Đóng vai là một chuyên gia định giá bất động sản tại Vinhomes Ocean Park. 
        Tôi có một căn hộ với thông số: diện tích {prop.area_m2}m2, {prop.num_bedrooms} phòng ngủ, tầng {prop.num_floors}, thuộc phân khu {prop.phan_khu}, view {prop.view}, tình trạng nội thất {prop.furniture}.
        Mô hình AI vừa định giá căn này là {price_bn} Tỷ VNĐ.
        Hãy viết 1 đoạn ngắn (khoảng 3-4 câu) giải thích cho khách hàng lý do căn hộ có mức giá này. Giọng điệu chuyên nghiệp, phân tích hợp lý theo thực tế thị trường.
        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Không thể tạo lời giải thích do lỗi kết nối AI: {str(e)}"

@app.post("/predict")
def predict_price(prop: PropertyInput):
    if model is None or encoders is None:
        raise HTTPException(status_code=500, detail="Model is not loaded. Run the training script first.")
        
    try:
        encoded_features = {}
        for col in ['phan_khu', 'view', 'furniture']:
            le = encoders.get(col)
            if prop.dict()[col] in le.classes_:
                encoded_features[col + '_encoded'] = le.transform([prop.dict()[col]])[0]
            else:
                encoded_features[col + '_encoded'] = 0 
                
        X = pd.DataFrame([{
            'area_m2': prop.area_m2,
            'num_floors': prop.num_floors,
            'num_bedrooms': prop.num_bedrooms,
            'phan_khu_encoded': encoded_features['phan_khu_encoded'],
            'view_encoded': encoded_features['view_encoded'],
            'furniture_encoded': encoded_features['furniture_encoded']
        }])
        
        price_bn = model.predict(X)[0]
        price_bn_rounded = round(float(price_bn), 2)
        
        explanation = generate_explanation(prop, price_bn_rounded)
        
        return {
            "status": "success",
            "input": prop.dict(),
            "predicted_price_bn": price_bn_rounded,
            "explanation": explanation
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
