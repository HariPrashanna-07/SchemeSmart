from fastapi import FastAPI
from backend.routes.schemes import router as scheme_router
from backend.routes.upload import router as upload_router
from backend.routes.eligibility import router as eligibility_router
from backend.routes.analyze import router as analyze_router

app = FastAPI()

app.include_router(analyze_router)
app.include_router(scheme_router)
app.include_router(upload_router)
app.include_router(eligibility_router)

@app.get("/")
def home():
    return {"status": "System Running"}