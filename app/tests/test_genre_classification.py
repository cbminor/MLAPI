from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

MYSTERY_BOOK_DESCRIPTION = "When a small-town detective uncovers a web of lies and betrayal, every clue pulls her deeper into a deadly game where trust is the most dangerous weapon."
ROMANCE_BOOK_DESCRIPTION = "Two strangers with broken pasts cross paths by chance, igniting a love that challenges their fears, heals old wounds, and changes everything they thought they knew about forever."

def test_lr_get_book_genres():
    response = client.post(
        "/classification/book-genres/",
        headers={"X-Token": "coneofsilence"},
        json={"description": ROMANCE_BOOK_DESCRIPTION, "method": "LR", "cutoff": 0.4},
    )
    assert response.status_code == 200
    assert response.json() == {
  "primary_labels": [
    "Romance",
    "Contemporary"
  ]
}
    
def test_bert_get_book_genres():
    response = client.post(
        "/classification/book-genres/",
        headers={"X-Token": "coneofsilence"},
        json={"description": MYSTERY_BOOK_DESCRIPTION, "method": "BERT", "cutoff": 0.5},
    )
    assert response.status_code == 200
    assert response.json() == {
  "primary_labels": [
    "Mystery",
    "Thriller"
  ]
}
    
def test_error_on_invalid_method():
    response = client.post(
        "/classification/book-genres/",
        headers={"X-Token": "coneofsilence"},
        json={"description": MYSTERY_BOOK_DESCRIPTION, "method": "INVALID", "cutoff": 0.5},
    )
    assert response.status_code == 422
    assert response.json() == {
  "detail": [
    {
      "type": "literal_error",
      "loc": [
        "body",
        "method"
      ],
      "msg": "Input should be 'LR' or 'BERT'",
      "input": "INVALID",
      "ctx": {
        "expected": "'LR' or 'BERT'"
      }
    }
  ]
}
    
def test_no_genres_found():
    response = client.post(
        "/classification/book-genres/",
        headers={"X-Token": "coneofsilence"},
        json={"description": ROMANCE_BOOK_DESCRIPTION, "method": "BERT", "cutoff": 1.0},
    )
    assert response.status_code == 200
    assert response.json() == {
  "primary_labels": []
}
