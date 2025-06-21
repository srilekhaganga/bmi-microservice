from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the BMI Classifier API. Go to /docs to try it out."}

class BMIInput(BaseModel):
    weight: float
    height: float

@app.post("/predict-bmi")
def predict_bmi(data: BMIInput):
    bmi = data.weight / (data.height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return {"bmi": round(bmi, 2), "category": category}

