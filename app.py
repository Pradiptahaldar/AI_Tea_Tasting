import streamlit as st
import pandas as pd
import time
import joblib

# 🎨 PAGE CONFIG
st.set_page_config(page_title="Tea Taster AI", page_icon="🍵", layout="centered")

# 🎨 Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #E8F5E9, #C8E6C9);
}
h1, h2, h3 {
    color: #4E342E;
    font-family: 'Segoe UI', sans-serif;
}
p, label, div {
    color: #6D4C41;
    font-size: 16px;
}
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

# 🏷️ TITLE
st.title("🍵 AI Tea Taster")
st.caption("Smart tea quality prediction system")

# 📊 LOAD DATA
@st.cache_data
def load_data():
    return pd.read_csv("./data/dataset.csv")

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

# 🔴 LOAD MODEL (INSTEAD OF TRAINING)
@st.cache_resource
def load_model():
    model = joblib.load("./models/model.pkl")
    encoder = joblib.load("./models/encoder.pkl")
    return model, encoder

model, le = load_model()

# 🧾 SESSION STATE INIT
if "history" not in st.session_state:
    st.session_state.history = []

if "result" not in st.session_state:
    st.session_state.result = None

if "confidence" not in st.session_state:
    st.session_state.confidence = None

# 🎛️ INPUT UI
st.subheader("Enter Tea Parameters")

temperature = st.slider("Temperature (°C)", 60, 100, 80)
ph = st.slider("pH Level", 4.5, 7.5, 6.5)
color_score = st.slider("Color Score", 1, 10, 5)

# 🚀 PREDICT BUTTON
if st.button("Predict Quality"):
    with st.spinner("Analyzing tea... ☕ Please wait..."):
        time.sleep(1.5)

        input_data = pd.DataFrame(
            [[temperature, ph, color_score]],
            columns=['temperature', 'ph', 'color_score']
        )

        prediction = model.predict(input_data)
        st.session_state.result = le.inverse_transform(prediction)[0]

        probs = model.predict_proba(input_data)
        st.session_state.confidence = max(probs[0]) * 100

        # Save history
        st.session_state.history.append({
            "Temp": temperature,
            "pH": ph,
            "Color": color_score,
            "Result": st.session_state.result,
            "Confidence": round(st.session_state.confidence, 2)
        })

# 🎨 SHOW RESULT (SAFE)
if st.session_state.result is not None:

    result = st.session_state.result
    confidence = st.session_state.confidence

    if result.lower() == "good":
        st.success(f"Predicted Quality: **{result.upper()}**")
    elif result.lower() == "average":
        st.warning(f"Predicted Quality: **{result.upper()}**")
    elif result.lower() == "bad":
        st.error(f"Predicted Quality: **{result.upper()}**")
    elif result.lower() == "excellent":
        st.success(f"Predicted Quality: **{result.upper()}**")
    else:
        st.write(f"Predicted Quality: {result}")

    st.info(f"Confidence: {confidence:.2f}%")

# 📜 HISTORY
st.subheader("Prediction History")

if st.session_state.history:
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)
else:
    st.write("No predictions yet.")

# 🔄 RESET
if st.button("Reset App"):
    st.session_state.history = []
    st.session_state.result = None
    st.session_state.confidence = None
    st.rerun()