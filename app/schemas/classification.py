from pydantic import BaseModel
from typing import List, Literal


class BookClassificationRequest(BaseModel):
    description: str
    method: Literal["LR", "BERT"]
    cutoff: float = 0.4

class BookClassificationResponse(BaseModel):
    primary_labels: List[str]
