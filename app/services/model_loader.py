import joblib
from functools import lru_cache
from pathlib import Path
import cloudpickle
import pickle
from app.models.model_loader import spaces

@lru_cache
def load_pickle_model(model_path: str):
    bytes_stream = spaces.get_file(model_path)
    model = pickle.load(bytes_stream)
    return model

@lru_cache
def load_joblib_model(model_path: str):
    bytes_stream = spaces.get_file(model_path)
    model_serialized = joblib.load(bytes_stream)
    model = cloudpickle.loads(model_serialized)
    return model



