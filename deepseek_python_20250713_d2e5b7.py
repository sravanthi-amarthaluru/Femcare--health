import joblib
import numpy as np

def predict_risk(features: dict) -> dict:
    model = joblib.load('model/pcos_model.joblib')
    scaler = joblib.load('model/scaler.joblib')
    
    # Prepare input features
    input_data = [
        features['age'],
        features['bmi'],
        features['irregular_cycles'],
        features['hair_growth'],
        features['acne_severity']
    ]
    
    scaled_data = scaler.transform([input_data])
    probabilities = model.predict_proba(scaled_data)[0]
    
    return {
        'Low': probabilities[0],
        'Medium': probabilities[1],
        'High': probabilities[2],
        'predicted_class': model.predict(scaled_data)[0]
    }