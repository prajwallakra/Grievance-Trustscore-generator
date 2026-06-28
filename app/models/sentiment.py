from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class SentimentModel:

    def __init__(self):
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

        print("Loading Sentiment Model...")

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name
        )

        print("Sentiment Model Loaded Successfully!")

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

        labels = ["Negative", "Neutral", "Positive"]

        return {
            "label": labels[predicted_class],
            "confidence": round(confidence, 4)
        }