import re
import json
from pathlib import Path

class TrustScoreEngine:
    def __init__(self):
        config_path = (
            Path(__file__)
            .resolve()
            .parents[2]
            / "config"
            / "trust_score.json"
        )
        with open(config_path, "r") as file:
            self.config = json.load(file)
        self.repeat_keywords = self.config["repeatKeywords"]


    def calculate(
        self,
        sentiment_label: str,
        emotion_label: str,
        severity_label: str,
        description: str
    ):
        score = self.config["base_score"]

        sentiment_penalty = self.config["sentiment"]
        score -= sentiment_penalty.get(sentiment_label, 0)

        emotion_penalty = self.config["emotion"]
        score -= emotion_penalty.get(emotion_label, 0)

        severity_penalty = self.config["severity"]
        score -= severity_penalty.get(severity_label, 0)

        text = description.lower()

        repeat_detected = any(
            keyword in text
            for keyword in self.repeat_keywords
        )

        if repeat_detected:
            score -= self.config["repeatComplaintPenalty"]

        score = max(0, min(score, 100))

        if score >= 81:
            level = "Very High"
        elif score >= 61:
            level = "High"
        elif score >= 41:
            level = "Moderate"
        elif score >= 21:
            level = "Low"
        else:
            level = "Very Low"
        return {
            "score": score,
            "level": level
        }
if __name__ == "__main__":

    engine = TrustScoreEngine()

    result = engine.calculate(
        sentiment_label="Negative",
        emotion_label="Anger",
        severity_label="High",
        description="No water for three days. This is my third complaint."
    )

    print(result)