from flask import Flask, render_template, request
from deepface import DeepFace
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Analyze emotions
        result = DeepFace.analyze(img_path=filepath, actions=['emotion'])
        dominant_emotion = result[0]['dominant_emotion']

        return render_template('index.html', emotion=dominant_emotion, image_path=filepath)
    return render_template('index.html', emotion="No file uploaded")

if __name__ == '__main__':
    app.run(debug=True)
