import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model + feature columns
model = pickle.load(open("final_model.sav", "rb"))
feature_cols = pickle.load(open("final_features.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def predict():

    # Collecting raw inputs from form
    data = {
        'SeniorCitizen': int(request.form['query1']),
        'MonthlyCharges': float(request.form['query2']),
        'TotalCharges': float(request.form['query3']),
        'gender': request.form['query4'],
        'Partner': request.form['query5'],
        'Dependents': request.form['query6'],
        'PhoneService': request.form['query7'],
        'MultipleLines': request.form['query8'],
        'InternetService': request.form['query9'],
        'OnlineSecurity': request.form['query10'],
        'OnlineBackup': request.form['query11'],
        'DeviceProtection': request.form['query12'],
        'TechSupport': request.form['query13'],
        'StreamingTV': request.form['query14'],
        'StreamingMovies': request.form['query15'],
        'Contract': request.form['query16'],
        'PaperlessBilling': request.form['query17'],
        'PaymentMethod': request.form['query18'],
        'tenure_group': get_tenure_group(int(request.form['query19']))
    }

    # Converting to DataFrame
    df = pd.DataFrame([data])

    # Converting categorical to dummy columns
    df_encoded = pd.get_dummies(df)

    # Aligning dummy columns with model
    df_final = df_encoded.reindex(columns=feature_cols, fill_value=0)

    prediction = model.predict(df_final)[0]
    probability = model.predict_proba(df_final)[0][1] * 100

    if prediction == 1:
        o1 = "⚠️ Customer is likely to CHURN!"
        o2 = f"Confidence: {probability:.2f}%"
    else:
        o1 = "✅ Customer is likely to STAY."
        o2 = f"Confidence: {100 - probability:.2f}%"

    return render_template("home.html", output1=o1, output2=o2)

# Generating tenure group
def get_tenure_group(tenure):

    if 1 <= tenure <= 12:
        return "1 - 12"
    elif 13 <= tenure <= 24:
        return "13 - 24"
    elif 25 <= tenure <= 36:
        return "25 - 36"
    elif 37 <= tenure <= 48:
        return "37 - 48"
    elif 49 <= tenure <= 60:
        return "49 - 60"
    else:
        return "61 - 72"

if __name__ == "__main__":
    app.run(debug=True)
