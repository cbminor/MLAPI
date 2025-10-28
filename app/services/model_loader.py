import io
import joblib
from functools import lru_cache
import pathlib
import cloudpickle
import pickle
from app.models.model_loader import spaces

class CrossPlatformUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "pathlib" and name == "WindowsPath":
            return pathlib.PosixPath
        return super().find_class(module, name)

@lru_cache
def load_pickle_model(model_path: str):
    bytes_stream = spaces.get_file(model_path)
    model = CrossPlatformUnpickler(bytes_stream).load()
    return model

@lru_cache
def load_joblib_model(model_path: str):
    # Step 1: Download the file from Spaces
    bytes_stream = spaces.get_file(model_path)

    # Step 2: Ensure we have a BytesIO stream (joblib requires file-like)
    if not isinstance(bytes_stream, io.BytesIO):
        bytes_stream = io.BytesIO(bytes_stream)

    # Step 3: First load the serialized model (via joblib)
    try:
        model_serialized = joblib.load(bytes_stream)
    except Exception as e:
        # Fallback: use cross-platform unpickler directly
        bytes_stream.seek(0)
        model_serialized = CrossPlatformUnpickler(bytes_stream).load()

    # Step 4: Then load the inner model (via cloudpickle)
    if isinstance(model_serialized, (bytes, bytearray)):
        model = cloudpickle.loads(model_serialized)
    else:
        model = model_serialized  # already unpickled object

    return model



