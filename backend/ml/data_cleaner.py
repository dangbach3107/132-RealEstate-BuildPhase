import pandas as pd
import re
import numpy as np

class DataCleaner:
    def __init__(self):
        pass

    def parse_price(self, text):
        if pd.isna(text):
            return np.nan
        text = str(text).lower()
        numbers = re.findall(r"[\d\,]+", text)
        if not numbers:
            return np.nan
        try:
            num = float(numbers[0].replace(',', '.'))
        except ValueError:
            return np.nan
            
        if 'tỷ' in text:
            return num
        elif 'triệu' in text:
            return num / 1000.0
        return np.nan

    def parse_area(self, text):
        if pd.isna(text):
            return np.nan
        text = str(text).lower()
        numbers = re.findall(r"[\d\,]+", text)
        if not numbers:
            return np.nan
        try:
            return float(numbers[0].replace(',', '.'))
        except ValueError:
            return np.nan

    def parse_number(self, text):
        if pd.isna(text):
            return np.nan
        text = str(text)
        numbers = re.findall(r"\d+", text)
        if not numbers:
            return np.nan
        return float(numbers[0])

    def clean_data(self, df):
        df['price_bn'] = df['price'].apply(self.parse_price)
        df['area_m2'] = df['area'].apply(self.parse_area)
        df['num_floors'] = df['floors'].apply(self.parse_number)
        df['num_bedrooms'] = df['bedrooms'].apply(self.parse_number)
        
        # Drop rows missing crucial info
        df = df.dropna(subset=['price_bn', 'area_m2'])
        
        df['num_floors'] = df['num_floors'].fillna(df['num_floors'].median())
        df['num_bedrooms'] = df['num_bedrooms'].fillna(df['num_bedrooms'].median())
        
        # New features from VOP Dataset
        features = ['area_m2', 'num_floors', 'num_bedrooms', 'price_bn']
        if 'phan_khu' in df.columns:
            features.extend(['phan_khu', 'view', 'furniture'])
            
        return df[features]
