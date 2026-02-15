from fastapi import FastAPI
from pydantic import BaseModel, Field 
import pandas as pd
from app.model.model import predict

app = FastAPI()

class ChurnInput(BaseModel):
    customer_id: str = Field(alias="CustomerID")
    count: int = Field(alias="Count")
    country: str = Field(alias="Country")
    state: str = Field(alias="State")
    city: str = Field(alias="City")
    zip_code: int = Field(alias="Zip Code")
    lat_long: str = Field(alias="Lat Long")
    latitude: float = Field(alias="Latitude")
    longitude: float = Field(alias="Longitude")
    gender: str = Field(alias="Gender")
    senior_citizen: str = Field(alias="Senior Citizen")
    partner: str = Field(alias="Partner")
    dependents: str = Field(alias="Dependents")
    tenure_months: int = Field(alias="Tenure Months")
    phone_service: str = Field(alias="Phone Service")
    multiple_lines: str = Field(alias="Multiple Lines")
    internet_service: str = Field(alias="Internet Service")
    online_security: str = Field(alias="Online Security")
    online_backup: str = Field(alias="Online Backup")
    device_protection: str = Field(alias="Device Protection")
    tech_support: str = Field(alias="Tech Support")
    streaming_tv: str = Field(alias="Streaming TV")
    streaming_movies: str = Field(alias="Streaming Movies")
    contract: str = Field(alias="Contract")
    paperless_billing: str = Field(alias="Paperless Billing")
    payment_method: str = Field(alias="Payment Method")
    monthly_charges: float = Field(alias="Monthly Charges")
    total_charges: str = Field(alias="Total Charges")
    
    class Config:
        populate_by_name = True

class PredictionOut(BaseModel):
    churn: int  

@app.get("/")
def home():
    return {'health_check': 'OK'}  

@app.post("/predict", response_model=PredictionOut) 
def predict_churn(data: ChurnInput):
    # Usar model_dump(by_alias=True) para obtener nombres originales con espacios
    df = pd.DataFrame([data.model_dump(by_alias=True)]) 
    prediction = predict(df)
    return {'churn': int(prediction[0])}