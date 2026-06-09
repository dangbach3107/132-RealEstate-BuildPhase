import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from data_cleaner import DataCleaner

def train_model():
    # 1. Load data
    data_path = os.path.join(os.path.dirname(__file__), '../../data/real_estate_raw.csv')
    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}")
        return

    df = pd.read_csv(data_path)
    
    # 2. Clean data
    cleaner = DataCleaner()
    df_clean = cleaner.clean_data(df)
    
    if len(df_clean) < 10:
        print("Not enough data after cleaning to train a model.")
        return

    # 3. Encode categorical features
    le = LabelEncoder()
    df_clean['district_encoded'] = le.fit_transform(df_clean['district'])
    
    # Save encoder
    joblib.dump(le, os.path.join(os.path.dirname(__file__), 'encoder.pkl'))
    
    # 4. Prepare X and y
    X = df_clean[['area_m2', 'num_floors', 'num_bedrooms', 'district_encoded']]
    y = df_clean['price_bn']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 5. Train model
    model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"Model trained successfully on {len(df_clean)} samples.")
    print(f"R2 Score on Test Set: {r2:.2f}")
    
    # 6. Save model
    joblib.dump(model, os.path.join(os.path.dirname(__file__), 'model.pkl'))
    print("Model and Encoder saved to backend/ml/")

if __name__ == '__main__':
    train_model()
