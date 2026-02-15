# Churn Prediction API

API REST para predecir churn de clientes usando XGBoost y FastAPI.

## 🚀 Instalación

### Opción 1: Docker
```bash
# Clonar repositorio
git clone https://github.com/Kento-kg/churn-api.git
cd churn-api

# Construir y ejecutar con Docker
docker build -t churn-api .
docker run -d -p 8000:8000 churn-api

# Detener el contenedor
docker stop churn-api-container

# Eliminar el contenedor
docker rm -f churn-api-container

# Eliminar la imagen
docker rmi churn-api:latest

# Con docker-compose
docker-compose up -d

# Acceder a la documentación
http://localhost:8000/docs

# Detener 
docker-compose down
```

### Opción 2: Local
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
uvicorn app.main:app --reload
```

## 📖 Uso

### Health Check
```bash
curl http://localhost:8000/
```

### Predicción
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
{
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
  "Total Charges": "29.85"
}
  }'
```

## 🐳 Docker

### Comandos útiles
```bash
# Ver logs
docker logs -f <container-id>

# Detener
docker stop <container-id>

# Eliminar
docker rm <container-id>
```

## 📁 Estructura del proyecto
```
├── app/
│   ├── main.py
│   └── model/
│       ├── model.py
│       ├── preprocessing.py
│       └── xgb_pipeline-0.1.0.pkl
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```