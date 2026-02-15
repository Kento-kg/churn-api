import pickle
from pathlib import Path
from app.model.preprocessing import CustomPreprocessor

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f'{BASE_DIR}/xgb_pipeline-0.1.0.pkl', 'rb') as f:
    pipeline = pickle.load(f)

def predict(data):
    pred = pipeline.predict(data)
    return pred