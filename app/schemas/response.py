from pydantic import BaseModel


class Sentiment(BaseModel):
    label: str
    confidence: float


class Emotion(BaseModel):
    label: str
    confidence: float


class Severity(BaseModel):
    label: str
    score: int


class TrustScore(BaseModel):
    score: int
    level: str


class Analysis(BaseModel):
    language: str
    translatedText: str
    sentiment: Sentiment
    emotion: Emotion
    severity: Severity
    trustScore: TrustScore
    priority: str
    summary: str

class ComplaintResponse(BaseModel):
    grievanceId: str
    complaintId: str

    analysis: Analysis