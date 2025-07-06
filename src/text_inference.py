import joblib
import numpy as np

model = joblib.load("models/text_model.pkl")
vectorizer = joblib.load("models/text_vectorizer.pkl")

def predict_text(text):
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    prob = np.max(model.predict_proba(X))
    return pred, prob