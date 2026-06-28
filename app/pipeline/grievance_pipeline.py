from app.schemas.request import ComplaintRequest
from app.models.emotion import EmotionModel
from app.schemas.response import (
    ComplaintResponse,
    Analysis,
    Sentiment,
    Emotion,
    Severity,
    TrustScore,
)
from app.services.priority import PriorityEngine
from app.models.sentiment import SentimentModel
from app.models.translator import Translator
from app.models.language_detector import LanguageDetector
from app.services.severity import SeverityEngine
from app.services.trust_score import TrustScoreEngine
class GrievancePipeline:
    def __init__(self):

        print("Initializing Pipeline...")

        self.sentiment_model = SentimentModel()
        self.emotion_model = EmotionModel()
        self.translator = Translator()
        self.language_detector = LanguageDetector()
        self.severity_engine = SeverityEngine()
        self.trust_score_engine = TrustScoreEngine()
        self.priority_engine = PriorityEngine()
        print("Pipeline Ready!")


    def process(self, request: ComplaintRequest) -> ComplaintResponse:
        language = self.language_detector.analyze(request.description)
        translated = self.translator.translate(
            request.description,
            language["language"]
        )
        sentiment = self.sentiment_model.analyze(translated)
        emotion = self.emotion_model.analyze(translated)
        severity = self.severity_engine.calculate(
            category=request.category,
            sentiment=sentiment["label"],
            emotion=emotion["label"],
            description=translated
        )
        trust_score = self.trust_score_engine.calculate(
            sentiment_label=sentiment["label"],
            emotion_label=emotion["label"],
            severity_label=severity["label"],
            description=translated
        )
        priority = self.priority_engine.calculate(
            severity_label=severity["label"],
            trust_score=trust_score["score"]
        )

        ##OUTPUTS####

        analysis = Analysis(
            language=language["language"],
            translatedText=translated,
            sentiment=Sentiment(**sentiment),
            emotion=Emotion(**emotion),
            severity=Severity(**severity),
            trustScore=TrustScore(**trust_score),
            priority=priority
        )

        return ComplaintResponse(
            grievanceId=request.grievanceId,
            complaintId=request.complaintId,
            analysis=analysis
        )