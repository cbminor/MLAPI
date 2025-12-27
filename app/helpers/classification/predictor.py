from pathlib import Path
from app.services.model_loader import load_joblib_model_local, load_pickle_model
from app.core.config import settings


# --- Initialize paths ---
# MODEL_DIR = "classification"

LR_MODEL_PATH = "../models/classification/lr_genre_classifier.joblib"
BERT_MODEL_PATH = "classification/distilbert_genre_classification.pkl"


# --- Load models once ---
lr_model = load_joblib_model_local(str(LR_MODEL_PATH))
bert_model = load_pickle_model(str(BERT_MODEL_PATH))


# --- Prediction logic ---
def predict_book_genre(description: str, method: str, cutoff: float):
    """
    Perform classification using either Logistic Regression or BERT.

    Args:
        description (str): Text input to classify
        method (str): 'LR' or 'BERT'
        cutoff (float): Cutoff value to choose which recommendations to show

    Returns:
        dict: { 'primary_labels': str }
    """

    if method == "LR":
        prediction = lr_model.predict_proba(description)
        classes = lr_model.classes_
        true_proba = [x[0][1] for x in prediction]
        mask = [x > cutoff for x in true_proba]
        labels = [d for d, m in zip(classes, mask) if m]
        return {"primary_labels": labels}

    elif method == "BERT":
        prediction = bert_model(description)
        labels = [x['label'] for x in prediction[0] if x['score'] > cutoff]

        return {"primary_labels": labels}

    else:
        raise ValueError(f"Unsupported method: {method}")
