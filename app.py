from flask import Flask, redirect, render_template, request, flash
import pickle as pkl
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

app = Flask(__name__)
app.secret_key = 'jhbfbbvibrkskfbdn(rishukumargupta8409+('

# Initialize error messages as empty strings
model_error_message = ""
cv_error_message = ""

# Load the trained model
try:
    with open("models/bagging_sentimnente.pkl", "rb") as model_file:
        model = pkl.load(model_file)
except FileNotFoundError:
    model_error_message = "Model file not found. Please ensure the model file exists."
    model = None


# Load the CountVectorizer
try:
    with open("models/CountVectors.pkl", "rb") as cv_file:
        cv = pkl.load(cv_file)
except FileNotFoundError:
    cv_error_message = "CountVectorizer file not found. Please ensure the CountVectorizer file exists."
    cv = None

# Function to preprocess text by removing stopwords and converting to lowercase
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)


@app.route("/", methods=['GET', 'POST'])
def home():
    result = None
    if request.method == "POST":
        text = request.form.get("tweets")
        if text:
            # Preprocess the input text
            preprocessed_text = preprocess(text)
            if cv is not None:
                # Transform preprocessed text using CountVectorizer
                model_input = cv.transform([preprocessed_text])
                if model is not None:
                    # Predict sentiment
                    prediction = model.predict(model_input)
                    # Interpret prediction
                    result = "Positive" if prediction[0] == 1 else "Negative"
                else:
                    flash("Model is not available.")
            else:
                flash("CountVectorizer is not available.")
    return render_template('index.html', result=result, model_error_message=model_error_message, cv_error_message=cv_error_message)

if __name__ == "__main__":
    # Initialize NLTK resources if not already initialized
    if not nltk.data.find('tokenizers/punkt'):
        nltk.download('punkt')
    if not nltk.data.find('corpora/stopwords'):
        nltk.download('stopwords')
    app.run(debug=True, host='0.0.0.0')
