from pydantic import BaseModel

class IrisRequest(BaseModel):
    harga_petani_h_min_2: float
    harga_petani_h_min_3: float
    harga_petani_h_min_4: float
    
    harga_pasar_h_min_1: float
    harga_pasar_h_min_2: float
    harga_pasar_h_min_3: float
    
    bulan: int
    trend: int

class PredictionResponse(BaseModel):
    predict_result: int