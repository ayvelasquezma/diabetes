from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

class ApiInput(BaseModel):
    features: List[float]

class ApiOutput(BaseModel):
    outcome: int

app = FastAPI()
model = joblib.load("model.joblib")

# Reemplace esto con su implementación:
@app.post("/predict")
async def predict(data: ApiInput) -> ApiOutput:
    model = joblib.load("model.joblib")
    outcome = model.predict([data.features])
    prediction = ApiOutput(outcome=outcome)
    return prediction
