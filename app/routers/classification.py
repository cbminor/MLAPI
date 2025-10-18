from fastapi import APIRouter, HTTPException
from app.schemas.classification import BookClassificationRequest, BookClassificationResponse
from app.helpers.classification.predictor import predict_book_genre

router = APIRouter()

@router.post("/book-genres", response_model=BookClassificationResponse)
def classify_book_genre(payload: BookClassificationRequest):
    try:
        result = predict_book_genre(payload.description, payload.method, payload.cutoff)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
