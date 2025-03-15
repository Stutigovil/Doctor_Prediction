
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Extract hour and minute from login time
df["Hour"] = pd.to_numeric(df["Login Time"].str[:2], errors="coerce")
df["Minute"] = pd.to_numeric(df["Login Time"].str[3:5], errors="coerce")

# Drop invalid time values
df.dropna(subset=["Hour", "Minute"], inplace=True)

# Round hour based on minutes (if >= 30, round up)
df["Login Hour"] = np.where(df["Minute"] >= 30, df["Hour"] + 1, df["Hour"]) % 24

# Filter doctors with enough survey attempts
df = df[df["Count of Survey Attempts"] > 3]

# Features & Target
X = df[["Login Hour"]]
y = df["NPI"]

# Encode NPI
npi_encoder = LabelEncoder()
y_encoded = npi_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoder
joblib.dump(model, "doctor_model.pkl")
joblib.dump(npi_encoder, "npi_encoder.pkl")

print("Model training complete. Saved as 'doctor_model.pkl'.")

def predict_doctors(login_hour):
    """
    Returns doctors available within ±1 hour of login_hour.
    Also saves predictions to an Excel file.
    """
    valid_doctors = df[(df["Login Hour"] >= login_hour - 1) & (df["Login Hour"] <= login_hour + 1)]
    
    if valid_doctors.empty:
        return None

    result_df = valid_doctors[["NPI", "Speciality", "Region"]].drop_duplicates()

    # Save predictions to Excel
    result_filename = "doctor_predictions.xlsx"
    result_df.to_excel(result_filename, index=False)

    return result_df.to_dict(orient="records")
