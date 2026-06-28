from fastapi import FastAPI
from app.schemas.request import ComplaintRequest
from app.schemas.response import ComplaintResponse
from app.pipeline.grievance_pipeline import GrievancePipeline

pipeline = GrievancePipeline()

app = FastAPI(
    title="Grievance TrustScore Generator API",
    description="AI-powered API for analyzing citizen grievances and generating trust scores.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to the Grievance TrustScore Generator API!"}

@app.post("/analyze", response_model=ComplaintResponse)
def analyze(request: ComplaintRequest):
    return pipeline.process(request)