from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route('/emotionDetector')
def emotion_dec():
    text = request.args.get('text', 'I love my life')
    res = emotion_detector(text)
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