"""
Server module to run emotion detection app
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Function to analyze text
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        # Return a dictionary with values for all keys being None
        # response = {
        #     'anger': None,
        #     'disgust': None,
        #     'fear': None,
        #     'joy': None,
        #     'sadness': None,
        #     'dominant_emotion': None
        # }
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)
    # Check if the result is valid
    if not result:
        return jsonify({'error': 'Emotion detection failed'}), 500
    return result


@app.route("/")
def render_index_page():
    """
    function to display index.html
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
