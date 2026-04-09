import pickle
import numpy as np

with open("model/model_rf_cabai_tuned.pkl", "rb") as f:
    model = pickle.load(f)

def predict(features):
    prediction = model.predict(features)
    return {"predict=_result": int(prediction[0])}