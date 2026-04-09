from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from app.model import predict
import numpy as np

app = FastAPI()

class IrisRequest(BaseModel):
    harga_petani_h_min_2: float
    harga_petani_h_min_3: float
    harga_petani_h_min_4: float
    
    harga_pasar_h_min_1: float
    harga_pasar_h_min_2: float
    harga_pasar_h_min_3: float
    
    bulan: int
    trend: int

@app.get("/")
def root():
    return {"message": "ML is service running"}

@app.post("/predict")
def predict_api(data: IrisRequest):
    try:
        features = np.array([[
            data.harga_petani_h_min_2,
            data.harga_petani_h_min_3,
            data.harga_petani_h_min_4,
            data.harga_pasar_h_min_1,
            data.harga_pasar_h_min_2,
            data.harga_pasar_h_min_3,
            data.bulan,
            data.trend
        ]])
        
        return predict(features)
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))