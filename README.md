# 🚀 Grievance TrustScore Generator

An AI-powered grievance analysis system that processes citizen complaints and generates actionable insights such as sentiment, emotion, severity, trust score, and priority. The system is built using FastAPI, Hugging Face Transformers, and rule-based business logic.

---

# 📖 Overview

Government grievance portals receive thousands of complaints every day. Manually prioritizing and analyzing these complaints is time-consuming and inconsistent.

The **Grievance TrustScore Generator** automates this process by analyzing the complaint text using AI models and generating a structured response that helps government departments understand:

* Citizen sentiment
* Citizen emotion
* Severity of the grievance
* Trust score towards the concerned department
* Complaint priority

---

# ✨ Features

* 🌐 Language Detection
* 🌍 Hindi → English Translation
* 😊 Sentiment Analysis
* 😠 Emotion Detection
* ⚠️ Severity Assessment
* 🤝 Trust Score Generation
* 🚨 Priority Classification
* ⚡ FastAPI REST API
* 📄 JSON Input & Output

---

# 🏗️ System Architecture

```text
                Client / Backend
                      │
                      ▼
              FastAPI REST API
                      │
                      ▼
            Grievance Pipeline
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
Language         Translation      Sentiment
Detector                             Model
                                       │
                                       ▼
                                Emotion Model
                                       │
                                       ▼
                               Severity Engine
                                       │
                                       ▼
                             Trust Score Engine
                                       │
                                       ▼
                               Priority Engine
                                       │
                                       ▼
                              JSON Response
```

---

# 🤖 AI Models Used

| Module             | Technology                                       |
| ------------------ | ------------------------------------------------ |
| Language Detection | langdetect                                       |
| Translation        | deep-translator (Google Translator)              |
| Sentiment Analysis | cardiffnlp/twitter-roberta-base-sentiment-latest |
| Emotion Detection  | j-hartmann/emotion-english-distilroberta-base    |
| Severity           | Custom Rule-Based Engine                         |
| Trust Score        | Custom Rule-Based Engine                         |
| Priority           | Custom Rule-Based Engine                         |

---

# 📂 Project Structure

```text
Grievance-Trustscore-generator/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── pipeline/
│   ├── schemas/
│   ├── services/
│   └── utils/
│
├── config/
│   ├── severity.json
│   └── trust_score.json
│
├── docs/
├── tests/
├── data/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Grievance-Trustscore-generator.git
```

Navigate to the project directory:

```bash
cd Grievance-Trustscore-generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

API will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoint

## POST `/analyze`

### Sample Request

```json
{
  "grievanceId": "DEL-2026-WTR-0001",
  "complaintId": "UUID-001",
  "category": "Water",
  "subcategory": "No Water Supply",
  "description": "No water supply for three days. Nobody is responding.",
  "district": "North-West Delhi",
  "ward": "Uttam Nagar",
  "locationLat": 28.6219,
  "locationLng": 77.0545,
  "evidenceUrls": [],
  "preferredLanguage": "en",
  "isAnonymous": false,
  "mobile": "9876543210",
  "isVerifiedIdentity": false,
  "sourceChannel": "web",
  "linkToClusterId": null
}
```

### Sample Response

```json
{
  "grievanceId": "DEL-2026-WTR-0001",
  "complaintId": "UUID-001",
  "analysis": {
    "language": "en",
    "translatedText": "No water supply for three days. Nobody is responding.",
    "sentiment": {
      "label": "Negative",
      "confidence": 0.99
    },
    "emotion": {
      "label": "Anger",
      "confidence": 0.96
    },
    "severity": {
      "label": "High",
      "score": 82
    },
    "trustScore": {
      "score": 23,
      "level": "Low"
    },
    "priority": "High"
  }
}
```

---

# 🔄 AI Workflow

1. Receive complaint JSON.
2. Detect the language of the complaint.
3. Translate Hindi complaints to English (if required).
4. Perform sentiment analysis.
5. Detect the emotional tone.
6. Calculate grievance severity using configurable rules.
7. Generate the department trust score.
8. Determine complaint priority.
9. Return the structured JSON response.

---

# 🛠️ Technologies Used

* Python 3.13
* FastAPI
* Pydantic
* Hugging Face Transformers
* PyTorch
* langdetect
* deep-translator
* Uvicorn

---

# 🚀 Future Improvements

* Multi-language translation support
* Duplicate complaint detection
* Complaint clustering
* OCR for image evidence
* Speech-to-text support
* LLM-powered complaint summarization
* Dashboard and analytics
* Database integration
* Authentication and authorization
* Docker deployment

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed as an AI-powered grievance analysis system using Natural Language Processing and rule-based decision engines.
