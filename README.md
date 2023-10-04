# Sentiment Analysis for Tweets

![sentiment-icon-13](https://github.com/rkgupta7463/Sentiment-Analysis-for-tweets/assets/96177171/1c82f3bf-c16e-426b-9026-832a9be37032)

### Table of Contents
  1. Introduction
  2. Features
  3. Getting Started
     I. Prerequisites
     II. Installation
  4. Usage
  5. Project Structure
  6. Contributing
  7. License

## 1. Introduction
Sentiment Analysis for Tweets is a Python-based project that performs sentiment analysis on user-provided text, specifically tweets. The goal of this project is to determine whether a given tweet is positive or negative in sentiment.
Sentiment analysis, also known as opinion mining, is a natural language processing task that involves classifying text as positive, negative, or neutral based on the sentiment expressed within the text.

![image](https://github.com/rkgupta7463/Sentiment-Analysis-for-tweets/assets/96177171/f9be1377-7ed4-46b5-ab54-9a676a961bd8)

## 2. Features
  1. Sentiment analysis of tweets.
  2. Preprocessing of text data, including removal of stopwords and converting text to lowercase.
  3. Use of a pre-trained machine learning model for sentiment classification.
  4. Web-based user interface for text input and analysis.


## 3. Getting Started

  ### I. Prerequisites
  Before you begin, ensure you have met the following requirements:
  
  1. Python 3.x installed.
  2. Necessary Python packages installed (flask, pandas, numpy, nltk, etc.).
  3. Pre-trained model and CountVectorizer (available in the models directory).

  ### II. Installation
  
  To install and run this project, follow these steps:
  
  1. Clone this repository to your local machine using:

    git clone https://github.com/rkgupta7463/Sentiment-Analysis-for-Tweets.git

  2. Navigate to the project directory:

    cd Sentiment-Analysis-for-Tweets
  3. Install the required Python packages using:

    pip install -r requirements.txt

  4. Start the Flask web application:
     
    python app.py

  5. Access the application in your web browser at:

    http://localhost:5000

4. Usage

    Open the web application in your browser.

    Enter a tweet or text you want to analyze in the provided text area.

    Click the "Analyze" button to perform sentiment analysis.

    The application will display the sentiment result (Positive or Negative) on the webpage.

5. Project Structure

  The project directory is structured as follows:
  
    app.py: The main Flask application file.
    
    models/: Directory containing pre-trained models and CountVectorizer.
    
    static/: Static files (CSS, images, and JavaScript).
    
    templates/: HTML templates for the web application.
    
    img/: Images used in the README file.
    
    requirements.txt: List of Python dependencies.
  
