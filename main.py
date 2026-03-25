import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# ✅ Load dataset
data = pd.read_csv("dataset.csv")

# ✅ Features
X = data[['temperature', 'ph', 'color_score']]

# ✅ Target encoding
le = LabelEncoder()
y = le.fit_transform(data['quality'])

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# ✅ Model
model = RandomForestClassifier(n_estimators=50, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# ✅ Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# INPUT WITH VALIDATION
print("\nEnter tea parameters:")

try:
    temperature = float(input("Temperature: "))
    ph = float(input("pH: "))
    color_score = float(input("Color Score: "))
except ValueError:
    print("❌ Invalid input! Use numbers only.")
    exit()

# ✅ Define ranges (you can adjust these)
MIN_TEMP = -10
MAX_TEMP = 100

MIN_PH = 4.5
MAX_PH = 7.5

MIN_COLOR = 1
MAX_COLOR = 10

# ✅ Validation checks
if not (MIN_TEMP <= temperature <= MAX_TEMP):
    print(f"❌ Temperature must be between {MIN_TEMP} and {MAX_TEMP}")
    exit()

if not (MIN_PH <= ph <= MAX_PH):
    print(f"❌ pH must be between {MIN_PH} and {MAX_PH}")
    exit()

if not (MIN_COLOR <= color_score <= MAX_COLOR):
    print(f"❌ Color Score must be between {MIN_COLOR} and {MAX_COLOR}")
    exit()

# ✅ Convert to DataFrame
input_data = pd.DataFrame(
    [[temperature, ph, color_score]],
    columns=['temperature', 'ph', 'color_score']
)

# ✅ Prediction
prediction = model.predict(input_data)
result = le.inverse_transform(prediction)

print("\nPredicted Tea Quality:", result[0])