import streamlit as st
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# 🎨 PAGE CONFIG
st.set_page_config(page_title="Tea Taster AI", page_icon="🍵", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    
    /* Main background */
    .stApp {
        background: linear-gradient(to right, #E8F5E9, #C8E6C9);
    }

    /* Headings */
    h1, h2, h3 {
        color: #4E342E;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Normal text */
    p, label, div {
        color: #6D4C41;
        font-size: 16px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1B5E20;
    }

    </style>
""", unsafe_allow_html=True)

st.title("🍵 AI Tea Taster")
st.caption("Smart tea quality prediction system")
# 📊 LOAD DATA

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

data = load_data()


# ℹ️ INFO BOX

with st.expander("ℹ️ About this project"):
    st.write("""
    This AI model predicts tea quality based on:
    - Temperature
    - pH Level
    - Color Score

    Built using Random Forest Classifier.
    """)


# 📊 DATA PREVIEW

st.subheader("Dataset Preview")
st.dataframe(data.head())
# PREPROCESS

X = data[['temperature', 'ph', 'color_score']]

le = LabelEncoder()
y = le.fit_transform(data['quality'])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
#  MODEL
@st.cache_resource
def train_model():
    model = RandomForestClassifier(
        n_estimators=50,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

model = train_model()
# INPUT UI

st.subheader("Enter Tea Parameters")

temperature = st.slider("Temperature (°C)", 60, 100, 80)
ph = st.slider("pH Level", 4.5, 7.5, 6.5)
color_score = st.slider("Color Score", 1, 10, 5)

# 📜 HISTORY STORAGE
if "history" not in st.session_state:
    st.session_state.history = []

# 🚀 PREDICT
if st.button("Predict Quality"):

    with st.spinner("Analyzing tea... ☕ Please wait..."):
        time.sleep(1.5)  # 👈 makes spinner visible

        input_data = pd.DataFrame(
            [[temperature, ph, color_score]],
            columns=['temperature', 'ph', 'color_score']
        )

        prediction = model.predict(input_data)
        result = le.inverse_transform(prediction)[0]

        probs = model.predict_proba(input_data)
        confidence = max(probs[0]) * 100

        # Save history
        st.session_state.history.append({
            "Temp": temperature,
            "pH": ph,
            "Color": color_score,
            "Result": result,
            "Confidence": round(confidence, 2)
        })

    st.success(f"Predicted Quality: **{result.upper()}**")
    st.info(f"Confidence: {confidence:.2f}%")
#  HISTORY TABLE
st.subheader("Prediction History")
if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)
else:
    st.write("No predictions yet.")
#  RESET BUTTON
if st.button("Reset App"):
    st.session_state.history = []
    st.rerun()