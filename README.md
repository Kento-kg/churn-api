# Customer Churn Prediction API

> Machine learning-powered REST API for predicting customer churn

A production-ready FastAPI application that predicts customer churn using XGBoost, enabling data-driven retention strategies. Fully containerized with Docker for scalable deployment.

## Project Overview

This project analyzes **10,000+ customers** to predict churn probability and improve retention by **31%**. The end-to-end ML pipeline delivers actionable insights through a scalable REST API.

## Installation

### Option 1: Docker (Recommended)
```bash
# Clone repository
git clone https://github.com/Kento-kg/churn-api.git
cd churn-api

# Build and run with Docker
docker build -t churn-api .
docker run -d -p 8000:8000 --name churn-api-container churn-api

# Or with docker-compose
docker-compose up -d

# Access API documentation
http://localhost:8000/docs
```

### Option 2: Local Installation
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

## 📖 Usage

### Interactive API Documentation

Access the auto-generated Swagger UI at: **`http://localhost:8000/docs`**

### Health Check
```bash
curl http://localhost:8000/
# Response: {"health_check":"OK","model_version":"0.1.0"}
```

### Predict Customer Churn
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "CustomerID": "7590-VHVEG",
    "Count": 1,
    "Country": "United States",
    "State": "California",
    "City": "Los Angeles",
    "Zip Code": 90001,
    "Lat Long": "33.9731, -118.2479",
    "Latitude": 33.9731,
    "Longitude": -118.2479,
    "Gender": "Female",
    "Senior Citizen": "No",
    "Partner": "Yes",
    "Dependents": "No",
    "Tenure Months": 1,
    "Phone Service": "No",
    "Multiple Lines": "No phone service",
    "Internet Service": "DSL",
    "Online Security": "No",
    "Online Backup": "Yes",
    "Device Protection": "No",
    "Tech Support": "No",
    "Streaming TV": "No",
    "Streaming Movies": "No",
    "Contract": "Month-to-month",
    "Paperless Billing": "Yes",
    "Payment Method": "Electronic check",
    "Monthly Charges": 29.85,
    "Total Charges": "29.85",
    "CLTV": 3239
  }'

# Response: {"churn": 1}  # 1 = High Risk, 0 = Low Risk
```
## Model Training

The complete training process is documented in `notebooks/telco_churn.ipynb`:

- **Exploratory Data Analysis**: Identified key factors correlated with customer attrition
- **Data Cleaning**: Handled missing values and outliers
- **Feature Engineering**: Created behavioral indicators and interaction features
- **Hyperparameter Tuning**: GridSearchCV optimization
- **Customer Segmentation**: Clustering analysis for targeted retention strategies

## Key Insights

### Churn Indicators
- Contract type (month-to-month shows highest churn)
- Customer tenure (newer customers at higher risk)
- Monthly charges and payment method
- Service usage patterns (internet, streaming, support)

### Customer Segments
- **High-Risk**: Month-to-month contracts, high charges, low tenure
- **Stable**: Long-term contracts, multiple services, longer tenure
- **Growth Potential**: Mid-tenure, moderate usage, responsive to retention offers

### Retention Strategies
1. Incentivize long-term contracts
2. Improve onboarding for new customers
3. Target high-charge customers with loyalty programs
4. Enhance customer support for at-risk segments

## Project Structure
```
churn-api/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application
│   └── model/
│       ├── __init__.py
│       ├── model.py               # Prediction logic
│       ├── preprocessing.py       # Custom transformers
│       └── xgb_pipeline-0.1.0.pkl # Trained model
├── notebooks/
│   └── telco_churn.ipynb           # Training notebook
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Multi-container setup
├── .dockerignore                  # Docker ignore rules
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
