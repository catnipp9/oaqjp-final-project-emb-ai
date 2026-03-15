# 🧠 Emotion Detection Application

> An AI-powered web application that detects emotions from text using Watson NLP, packaged as a Python module and deployed via Flask.

**IBM Full Stack Developer Professional Certificate** · Coursera Final Project

---

## 📁 Project Structure

```
final_project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
├── README.md
└── ... other submission files
```

---

## ✨ Features

### 🔍 Emotion Detection
- Accepts any text input and returns confidence scores for five core emotions:
  - **Anger**, **Disgust**, **Fear**, **Joy**, **Sadness**
- Identifies the **dominant emotion** from the analysis.

### 🛡️ Error Handling
- Gracefully handles blank or invalid inputs.
- Returns `None` for all emotion scores when the input is empty.

### ✅ Unit Testing
- Includes five unit tests covering all emotion categories:

| Input | Expected Dominant Emotion |
|---|---|
| `"I am glad this happened"` | joy |
| `"I am really mad about this"` | anger |
| `"I feel disgusted just hearing about this"` | disgust |
| `"I am so sad about this"` | sadness |
| `"I am really afraid that this will happen"` | fear |

### 🌐 Web Deployment
- Deployed as a **Flask** web service on `localhost:5000`.
- Endpoint: `POST /emotionDetector`
- Accepts JSON input and returns a human-readable formatted response.

### 🧹 Static Code Analysis
- `server.py` analyzed with **PyLint**.
- Achieves a perfect score of **10/10**.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
pip install flask requests
```

> No additional setup is needed for Watson NLP — the libraries are embedded in the project.

### Run the Flask Server

```bash
python3 server.py
```

---

## 🧪 Usage

### Send a POST Request

```bash
curl -X POST http://localhost:5000/emotionDetector \
  -H "Content-Type: application/json" \
  -d '{"text": "I love learning new things"}'
```

### Example Response

```json
{
  "result": "For the given statement, the system response is 'anger': 0.003, 'disgust': 0.001, 'fear': 0.005, 'joy': 0.98, 'sadness': 0.011. The dominant emotion is joy."
}
```

### Run Unit Tests

```bash
python3 -m unittest test_emotion_detection.py
```

**Expected Output:**

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.512s

OK
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Flask** — Web framework
- **Watson NLP** — Emotion prediction engine
- **PyLint** — Static code analysis
- **unittest** — Testing framework

---

## 👤 Author

**Your Name**  
IBM Full Stack Developer Professional Certificate — Coursera
