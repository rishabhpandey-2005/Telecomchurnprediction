import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.combine import SMOTEENN
import pickle

# Load encoded dataset
df = pd.read_csv("tel_churn.csv")

# Drop unwanted column
df.drop(columns=["Unnamed: 0"], inplace=True)

# Features (all dummy columns) and target
X = df.drop(columns=["Churn"])
y = df["Churn"]

# SMOTEENN for balancing
smt = SMOTEENN()

X_resampled, y_resampled = smt.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=300, random_state=42)
model.fit(X_train, y_train)

# Save final model
pickle.dump(model, open("final_model.sav", "wb"))

# Save final feature columns
pickle.dump(X.columns.tolist(), open("final_features.pkl", "wb"))

print("✔ Training complete!")
print("✔ Saved: final_model.sav and final_features.pkl")
