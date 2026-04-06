import streamlit as st
import cv2
import numpy as np
from main import get_sensor_data, get_color_value, predict_quality

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Tea Quality Detector", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
}

.main-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #2d3436;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.stButton>button {
    background-color: #6c5ce7;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #4834d4;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="main-title">🍵 Tea Quality Detector</p>', unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

# ---------------- SENSOR CARD ----------------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📡 Sensor Data")

    if st.button("Get Sensor Data"):
        data = get_sensor_data()
        if data is not None:
            st.session_state['sensor'] = data

    if 'sensor' in st.session_state:
        temp, humidity, aroma = st.session_state['sensor']
        st.metric("🌡 Temperature", f"{temp:.2f}")
        st.metric("💧 Humidity", f"{humidity:.2f}")
        st.metric("👃 Aroma", f"{aroma:.2f}")
    else:
        st.info("Click button to fetch sensor data")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- IMAGE CARD ----------------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📷 Tea Image")

    uploaded_file = st.file_uploader("Upload Tea Image")

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(image, caption="Uploaded Tea", use_column_width=True)

        color = get_color_value(image)
        st.session_state['color'] = color

    if 'color' in st.session_state:
        st.metric("🎨 Color Value", f"{st.session_state['color']}")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🤖 Prediction")

if st.button("Predict Quality"):
    if 'sensor' in st.session_state and 'color' in st.session_state:
        temp, humidity, aroma = st.session_state['sensor']
        color = st.session_state['color']

        result = predict_quality(temp, humidity, aroma, color)

        st.success(f"🍵 Tea Quality: {result}")
    else:
        st.warning("⚠️ Complete all steps first")

st.markdown('</div>', unsafe_allow_html=True)
