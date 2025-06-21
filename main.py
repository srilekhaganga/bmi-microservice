from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BMIInput(BaseModel):
    height_cm: float
    weight_kg: float

@app.post("/bmi")
def calculate_bmi(data: BMIInput):
    height_m = data.height_cm / 100
    bmi = data.weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return {"bmi": round(bmi, 2), "category": category}
