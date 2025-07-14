from flask import Flask, render_template, request
import joblib
from extract_features import extract_features

app = Flask(__name__)
model = joblib.load('model/phishing_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    features = extract_features(url)
    prediction = model.predict([features])[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    return render_template('index.html', url=url, prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
