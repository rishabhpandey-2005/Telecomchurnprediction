
# Telecom Customer Churn Prediction

This project predicts whether a telecom customer is likely to churn based on usage patterns, account details, and service information. It includes end-to-end data analysis, feature engineering, model training, and a deployed Flask application that allows users to make real-time churn predictions.

Live Application: [https://telecomchurnprediction.onrender.com](https://telecomchurnprediction.onrender.com)
GitHub Repository: [https://github.com/rishabhpandey-2005/Telecomchurnprediction](https://github.com/rishabhpandey-2005/Telecomchurnprediction)

---

## 1. Project Overview

Customer churn is a significant problem in the telecom industry, leading to revenue loss. This project aims to build a machine learning model that can identify customers at risk of leaving the service.
The solution includes data preprocessing, model building, evaluation, and a web interface for making predictions.

---

## 2. Features

* Complete Exploratory Data Analysis (EDA)
* Data cleaning and feature engineering
* Machine learning model trained using Random Forest
* Saved model and feature mapping for consistent prediction
* Flask-based web interface for user input
* Public deployment using Render
* Simple and interactive UI for prediction results

---

## 3. Machine Learning Model

* Algorithm: Random Forest Classifier
* Model File: final_model.sav
* Feature Mapping: final_features.pkl
* Libraries used: scikit-learn, pandas, numpy

The model was trained after performing preprocessing steps such as encoding categorical variables and handling continuous values. It performs well on the given dataset and provides reliable churn predictions.

---

## 4. Dataset

The dataset used in this project is the Telco Customer Churn dataset.
It contains information such as:

* Customer demographics
* Tenure details
* Contract type
* Billing information
* Internet and phone services
* Support services
* Monthly and total charges
* Churn label (Yes or No)

---

## 5. Project Structure

```
Telecomchurnprediction/
│
├── app.py                     # Flask application
├── train_model.py             # Model training script
├── final_model.sav            # Saved machine learning model
├── final_features.pkl         # Encoded feature names
├── requirements.txt           # Project dependencies
├── runtime.txt                # Python version for deployment
├── Procfile                   # Render deployment file
├── templates/
│     └── index.html           # Web application UI
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── tel_churn.csv
└── first_telc.csv
```

---

## 6. Deployment Details

The application is deployed on Render as a web service.

Important deployment files:

### Procfile

```
web: gunicorn app:app
```

### runtime.txt

```
python-3.10.12
```

### requirements.txt

```
Flask==2.3.2
numpy
pandas
scikit-learn==1.5.1
gunicorn
joblib
```

---

## 7. How to Run Locally

Step 1: Clone the repository

```
git clone https://github.com/rishabhpandey-2005/Telecomchurnprediction.git
cd Telecomchurnprediction
```

Step 2: Install dependencies

```
pip install -r requirements.txt
```

Step 3: Run the Flask application

```
python app.py
```

Step 4: Open the application
Visit the following link in your browser:

```
http://127.0.0.1:5000/
```

---
## 8.Screenshot
<img width="1366" height="674" alt="Telecom Churn Prediction" src="https://github.com/user-attachments/assets/0eac1f87-f4c5-47fa-a776-f0b92f645bd4" />


## 9. Author

Rishabh Pandey
Final Year EXTC Student
Machine Learning and Data Science Enthusiast
GitHub: [https://github.com/rishabhpandey-2005](https://github.com/rishabhpandey-2005)

---

## 10. License

This project is open-source and available under the MIT License.

