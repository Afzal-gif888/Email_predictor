from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']

    # Convert text to vector
    msg_vec = vectorizer.transform([message])

    # Predict
    prediction = model.predict(msg_vec)

    if prediction[0] == 1:
        result = "Spam"
        prediction_class = "spam"
    else:
        result = "Not Spam"
        prediction_class = "not-spam"

    return render_template(
        'index.html',
        prediction=result,
        prediction_class=prediction_class
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)