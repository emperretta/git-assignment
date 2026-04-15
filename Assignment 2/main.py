from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model

app = FastAPI()

# Load the saved PyCaret pipeline
model = load_model('best_pipeline')

# Define the input data structure
class ClientData(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    balance: int
    housing: str
    loan: str
    contact: str
    day: int
    month: str
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str

@app.post("/predict")
def predict(data: ClientData):
    # Convert input to dataframe
    input_df = pd.DataFrame([data.dict()])
    # Run prediction
    prediction = predict_model(model, data=input_df)
    # Return result
    result = prediction['prediction_label'].iloc[0]
    return {"prediction": result}