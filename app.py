import streamlit as st
import cv2
import numpy as np
from main import get_sensor_data, get_color_value, predict_quality, get_accuracy

st.title("🍵 Tea Quality Detector")

# ---------------- ACCURACY ----------------
# st.write(f"📊 Model Accuracy: {get_accuracy()*100:.2f}%")

# ---------------- SENSOR ----------------
st.subheader("Sensor Data")

if st.button("Get Sensor Data"):
    data= get_sensor_data()
    if data is not None:
        temp, humidity, aroma = data            
    st.session_state['sensor'] = (temp, humidity, aroma)
else:
    st.warning("⚠️ Click the button to get sensor data")

if 'sensor' in st.session_state:
    temp, humidity, aroma = st.session_state['sensor']
    st.write(f"🌡 Temp: {temp:.2f}")
    st.write(f"💧 Humidity: {humidity:.2f}")
    st.write(f"👃 Aroma: {aroma:.2f}")

# ---------------- IMAGE ----------------
st.subheader("Tea Image")

uploaded_file = st.file_uploader("Upload Tea Image")

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption="Uploaded Tea")

    color = get_color_value(image)
    st.session_state['color'] = color

if 'color' in st.session_state:
    st.write(f"🎨 Color Value: {st.session_state['color']}")

# ---------------- PREDICTION ----------------
st.subheader("Prediction")

if st.button("Predict Quality"):
    if 'sensor' in st.session_state and 'color' in st.session_state:
        temp, humidity, aroma = st.session_state['sensor']
        color = st.session_state['color']

        result = predict_quality(temp, humidity, aroma, color)
        st.success(f"🍵 Tea Quality: {result}")
    else:
        st.warning("⚠️ Please complete all steps")