import serial
import time
import pandas as pd
import numpy as np
import cv2
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATASET ----------------
data = pd.read_csv("tea_dataset.csv")

X = data[['temp', 'humidity', 'aroma', 'color']]
y = data['quality']

# ---------------- TRAIN MODEL ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# ---------------- ACCURACY ----------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

def get_accuracy():
    return accuracy


# ---------------- SENSOR DATA ----------------

def get_sensor_data():

    # ✅ Initialize once
    if "ser" not in st.session_state:
        try:
            st.session_state.ser = serial.Serial('COM5', 115200, timeout=1)
            time.sleep(2)
        except:
            st.error("❌ COM5 busy. Close Arduino / restart")
            return None

    ser = st.session_state.ser

    # ✅ If port got corrupted, reopen cleanly
    if not ser.is_open:
        try:
            ser.open()
            time.sleep(2)
        except:
            st.error("❌ Failed to reopen COM5")
            return None

    readings = []

    try:
        ser.reset_input_buffer()

        while len(readings) < 5:
            line = ser.readline().decode(errors='ignore').strip()

            if line and "," in line:
                try:
                    temp, hum, aroma = map(float, line.split(","))
                    readings.append([temp, hum, aroma])
                except:
                    continue

    except:
        st.error("❌ Serial read failed. Replug ESP32")
        return None

    avg = np.mean(readings, axis=0)
    return avg


# ---------------- COLOR FROM IMAGE ----------------
def get_color_value(image):
    image = cv2.resize(image, (200, 200))

    h, w, _ = image.shape
    roi = image[h//3:h//2, w//3:w//2]

    avg_color = int(np.mean(roi))  # integer

    return avg_color


# ---------------- PREDICT ----------------
def predict_quality(temp, humidity, aroma, color):
    input_data = np.array([[temp, humidity, aroma, color]])
    prediction = model.predict(input_data)[0]
    return prediction