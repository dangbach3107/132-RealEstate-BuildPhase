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
    data_path = os.path.join(os.path.dirname(__file__), '../../data/vop_real_estate.csv')
    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}")
        return

    df = pd.read_csv(data_path)
    
    cleaner = DataCleaner()
    df_clean = cleaner.clean_data(df)
    
    if len(df_clean) < 10:
        print("Not enough data after cleaning to train a model.")
        return

    # Encode categorical features
    categorical_cols = ['phan_khu', 'view', 'furniture']
    encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        df_clean[col + '_encoded'] = le.fit_transform(df_clean[col])
        encoders[col] = le
        
    # Save encoders dictionary
    joblib.dump(encoders, os.path.join(os.path.dirname(__file__), 'encoder.pkl'))
    
    # Prepare X and y
    feature_cols = ['area_m2', 'num_floors', 'num_bedrooms', 
                   'phan_khu_encoded', 'view_encoded', 'furniture_encoded']
    X = df_clean[feature_cols]
    y = df_clean['price_bn']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestRegressor(n_estimators=150, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"Model trained successfully on {len(df_clean)} samples.")
    print(f"R2 Score on Test Set: {r2:.4f}")
    
    # Save model
    joblib.dump(model, os.path.join(os.path.dirname(__file__), 'model.pkl'))
    
    # Feature Importance
    importances = model.feature_importances_
    print("Feature Importances:")
    for feature, imp in zip(feature_cols, importances):
        print(f"  - {feature}: {imp:.4f}")

if __name__ == '__main__':
    train_model()
