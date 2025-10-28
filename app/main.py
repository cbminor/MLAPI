from fastapi import FastAPI
from app.routers import classification

app = FastAPI(title="ML Model API", version="1.0")

# Include Routers
app.include_router(classification.router, prefix="/classification", tags=["Classification"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
