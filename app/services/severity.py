import json
from pathlib import Path

DEFAULT_CATEGORY_SCORE = 10
class SeverityEngine:

    def __init__(self):
        config_path = (
            Path(__file__).resolve().parents[2]
            / "config"
            / "severity.json"
        )
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def calculate(
        self,
        category: str,
        sentiment: str,
        emotion: str,
        description: str
    ):

        score = self.config["base_score"]
        score += self.config["category"].get(category, DEFAULT_CATEGORY_SCORE)
        score += self.config["sentiment"].get(sentiment, 0)
        score += self.config["emotion"].get(emotion, 0)
        text = description.lower()
        for keyword, value in self.config["critical_keywords"].items():
            if keyword in text:
                score += value
        score = min(score, 100)
        if score >= 76:
            label = "Critical"
        elif score >= 51:
            label = "High"
        elif score >= 26:
            label = "Medium"
        else:
            label = "Low"
        return {
            "label": label,
            "score": score
        }
if __name__ == "__main__":
    engine = SeverityEngine()
    result = engine.calculate(
        category="Water",
        sentiment="Negative",
        emotion="Anger",
        description="No water for three days."
    )
    print(result)