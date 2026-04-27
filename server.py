from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_analyzer():
    text_to_analyze = request.form.get('text')
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Please provide text for analysis.", 400
    
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid input! Try again.", 400
    
    output = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    return output

if __name__ == '__main__':
    app.run(debug=True, port=5000)