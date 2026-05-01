import joblib
import pandas as pd

# Load trained model
model = joblib.load('models/churn_model.pkl')

def predict_churn(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    probability = model.predict_proba(df)

    return prediction[0], probability[0][1]