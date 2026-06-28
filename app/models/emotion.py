from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

import torch

class EmotionModel:

    def __init__(self):
        self.model_name = "j-hartmann/emotion-english-distilroberta-base"
        print("Loading Emotion Model...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name
        )
        print("Emotion Model Loaded Successfully!")

    def analyze(self, text: str):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )
        with torch.no_grad():
            outputs = self.model(**inputs)

        probabilities = torch.softmax(outputs.logits, dim=1)

        predicted_class = torch.argmax(probabilities).item()

        confidence = probabilities[0][predicted_class].item()

        label = self.model.config.id2label[predicted_class].lower()

        label_mapping = {
            "anger": "Anger",
            "disgust": "Frustration",
            "fear": "Fear",
            "sadness": "Disappointment",
            "neutral": "Neutral",
            "joy": "Neutral",
            "surprise": "Neutral"
        }
        return {
            "label": label_mapping.get(label, "Neutral"),
            "confidence": round(confidence, 4)
        }


if __name__ == "__main__":
    model = EmotionModel()
    test_text = "No water supply for three days. Nobody is responding."
    result = model.analyze(test_text)
    print(result)