

import traceback

print("Starting FastAPI...")
try:
    # put your existing imports below
    from fastapi import FastAPI
    from app.routers import classification
except Exception:
    traceback.print_exc()
    raise

app = FastAPI(title="ML Model API", version="1.0")

# Include Routers
app.include_router(classification.router, prefix="/classification", tags=["Classification"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
