from fastapi import APIRouter
import pickle
import numpy as np
from fastapi import Body

router = APIRouter(prefix="/predict", tags=["Prediction"])

with open("app/models/LogisticRegression_optimized.pkl", "rb") as f:
    model = pickle.load(f)

@router.post("/")
async def predict(features: list = Body(...)):
    prediction = model.predict(np.array(features).reshape(1, -1))
    return {"prediction": prediction.tolist()}
