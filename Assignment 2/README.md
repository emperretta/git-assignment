# Assignment 2: Automated ML Pipelines & Model Serving

## Overview
This project compares automated (PyCaret) and manual (scikit-learn) ML workflows 
for predicting whether a bank client will subscribe to a term deposit, using the 
UCI Bank Marketing dataset (45,211 rows, 17 features).

## Files
- `discovery.py` — Model comparison and evaluation
- `main.py` — FastAPI deployment
- `best_pipeline.pkl` — Saved PyCaret model pipeline
- `bank-full.csv` — Dataset

## Results
PyCaret identified LightGBM as the best model with 90.96% accuracy.
The manual scikit-learn implementation confirmed this with 91% accuracy.

## How to Run the API
```bash
uvicorn main:app --reload
```

## Sample API Input
```json
{
  "age": 35,
  "job": "management",
  "marital": "married",
  "education": "tertiary",
  "default": "no",
  "balance": 1500,
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "day": 15,
  "month": "may",
  "duration": 200,
  "campaign": 2,
  "pdays": -1,
  "previous": 0,
  "poutcome": "unknown"
}
```

## Sample API Output
```json
{
  "prediction": "no"
}
```