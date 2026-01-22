"""
server.py
Flask web server for the Emotion Detection application.
Accepts a sentence via query parameter and returns emotion scores and dominant emotion.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)
@app.route('/emotionDetector')
def emotion_dec():
    """Endpoint to analyze the emotion of a sentence."""
    text = request.args.get('text')
    res = emotion_detector(text)

    if res['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return (
        f"For the given statement, the system response is "
        f"anger: {res['anger']}, "
        f"disgust: {res['disgust']}, "
        f"fear: {res['fear']}, "
        f"joy: {res['joy']} and "
        f"sadness: {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
