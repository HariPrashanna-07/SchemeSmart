from fastapi import FastAPI
from backend.routes.schemes import router as scheme_router
from backend.routes.upload import router as upload_router

app = FastAPI()

app.include_router(scheme_router)
app.include_router(upload_router)

@app.get("/")
def home():
    return {"status": "System Running"}