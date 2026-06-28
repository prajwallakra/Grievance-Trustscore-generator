from app.models import sentiment
from app.schemas.request import ComplaintRequest

from app.schemas.response import (
    ComplaintResponse,
    Analysis,
    Sentiment,
    Emotion,
    Severity,
    TrustScore,
)

from app.models.sentiment import SentimentModel

class GrievancePipeline:
    def __init__(self):

        print("Initializing AI Pipeline...")

        self.sentiment_model = SentimentModel()

        print("Pipeline Ready!")


    def process(self, request: ComplaintRequest) -> ComplaintResponse:
        sentiment = self.sentiment_model.analyze(request.description)

        analysis = Analysis(
            language=request.preferredLanguage,
            translatedText=request.description,
            sentiment=Sentiment(**sentiment),
            emotion=Emotion(
                label="Anger",
                confidence=0.95
            ),
            severity=Severity(
                label="High",
                score=88
            ),
            trustScore=TrustScore(
                score=23,
                level="Low"
            ),
            priority="High",
            summary=request.description
        )

        return ComplaintResponse(
            grievanceId=request.grievanceId,
            complaintId=request.complaintId,
            analysis=analysis
        )