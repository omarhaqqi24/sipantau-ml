import joblib
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../model/model_rf_cabai_tuned.pkl")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

with open(MODEL_PATH, "rb") as f:
    model = joblib.load(f)
    if model is None:
        raise ValueError("Model failed to load")
    else:
        logger.info("Model loaded successfully")

def predict(features):
    prediction = model.predict(features)
    return {"predict_result": int(prediction[0])}