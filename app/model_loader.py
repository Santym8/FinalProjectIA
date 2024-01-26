# model_loader.py
from keras.models import load_model
import joblib

# Cargar el modelo y el escalador una sola vez al iniciar la aplicación
model = load_model("app/PredictionModel/model.h5")
min_max_scaler = joblib.load("app/PredictionModel/min_max_scaler.save")
