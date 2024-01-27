# model_loader.py
# from keras.models import load_model
import joblib

print("Cargando modelo y escalador...")
# Cargar el modelo y el escalador una sola vez al iniciar la aplicación
model = joblib.load("app/PredictionModel/model-10.h5")
min_max_scaler = joblib.load("app/PredictionModel/escalado-10.h5")

