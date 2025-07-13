import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_pcos_model():
    # Load your dataset here (replace with actual data)
    data = pd.read_csv('data/pcos_dataset.csv')
    
    X = data.drop('risk_level', axis=1)
    y = data['risk_level']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=7,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'model/pcos_model.joblib')
    return model