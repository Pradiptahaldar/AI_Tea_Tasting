import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
data = pd.read_csv("./data/dataset.csv")

# Features and target
X = data[['temperature', 'ph', 'color_score']]

le = LabelEncoder()
y = le.fit_transform(data['quality'])

# Train model
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=5,
    random_state=42
)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, "./models/model.pkl")
joblib.dump(le, "./models/encoder.pkl")

print("Model and encoder saved successfully.")