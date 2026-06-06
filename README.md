# Email Spam Detection using Naive Bayes

## Overview

This project is a Machine Learning based Email/SMS Spam Detection System developed using Python, Scikit-learn, Flask, HTML, and CSS.

The application classifies a message as either:

* Spam
* Not Spam

A Naive Bayes classifier is trained on a labeled dataset of spam and legitimate messages and deployed as a web application using Flask and Render.

## Features

* Spam message detection using Machine Learning
* Text preprocessing and vectorization
* Naive Bayes classification model
* Simple and responsive web interface
* Flask backend integration
* Deployed online using Render

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Flask
* HTML
* CSS
* Render

## Machine Learning Workflow

1. Load and clean dataset
2. Convert text into numerical features using CountVectorizer
3. Train a Multinomial Naive Bayes model
4. Save trained model using Pickle
5. Build Flask web application
6. Deploy application on Render

## Project Structure

Email_predictor/

├── app.py

├── spam_model.pkl

├── vectorizer.pkl

├── requirements.txt

├── templates/

│ └── index.html

└── static/

└── style.css

## Installation

Clone the repository:

```bash
git clone https://github.com/Afzal-gif888/Email_predictor.git
cd Email_predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Live Demo

https://email-predictor.onrender.com

## GitHub Repository

https://github.com/Afzal-gif888/Email_predictor

## Future Improvements

* TF-IDF Vectorization
* Deep Learning based classification
* User authentication
* Spam probability score
* Email attachment analysis

## Author

Afzal

B.Tech Student | Machine Learning Enthusiast | Aspiring Software Developer
