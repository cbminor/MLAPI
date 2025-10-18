import joblib
from functools import lru_cache
from pathlib import Path
import cloudpickle
import pickle

@lru_cache
def load_pickle_model(model_path: str):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

@lru_cache
def load_joblib_model(model_path: str):
    model_serialized = joblib.load(model_path)
    model = cloudpickle.loads(model_serialized)
    return model



