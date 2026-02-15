from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class CustomPreprocessor(BaseEstimator, TransformerMixin):
    """
    Preprocesador personalizado compatible con pickle.
    """
    
    def fit(self, X, y=None):
        # No necesita entrenar nada
        return self
    
    def transform(self, X):
        df = X.copy()
        
        # Total Charges: convertir espacios a 0 y luego a float
        df['Total Charges'] = df['Total Charges'].replace(' ', '0').astype(float)
        
        # Eliminar columnas no necesarias
        cols_to_drop = ['State', 'Country', 'Count', 'Zip Code', 
                        'Lat Long', 'Longitude', 'Latitude', 'CustomerID']
        df = df.drop(columns=[col for col in cols_to_drop if col in df.columns], errors='ignore')
        
        # Feature engineering: Has Internet
        df['Has_Internet'] = df['Internet Service'].apply(lambda x: 0 if x == 'No' else 1)
        
        # Reemplazar "No internet service" por "No"
        internet_cols = ['Online Security', 'Online Backup', 'Device Protection', 
                         'Tech Support', 'Streaming TV', 'Streaming Movies']
        for col in internet_cols:
            if col in df.columns:
                df[col] = df[col].replace('No internet service', 'No')
        
        # Reemplazar "No phone service" por "No"
        if 'Multiple Lines' in df.columns:
            df['Multiple Lines'] = df['Multiple Lines'].replace('No phone service', 'No')
        
        return df