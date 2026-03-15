"""
server.py

This file deploys the EmotionDetection application as a web service
using Flask. It exposes an endpoint /emotionDetector that accepts
POST requests with text and returns the dominant emotion along
with scores for anger, disgust, fear, joy, and sadness.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """Detect the dominant emotion from the input text and return a formatted response."""
    data = request.get_json()
    text_to_analyse = data.get("text", "")
    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        response_message = "Invalid text! Please try again!"
    else:
        response_message = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']}, "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return jsonify({"result": response_message})


if __name__ == "__main__":
    # Run the Flask server on localhost port 5000
    app.run(host="localhost", port=5000, debug=True)
    