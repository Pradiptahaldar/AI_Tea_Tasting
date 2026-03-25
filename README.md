# 🍵 AI Tea Quality Predictor

## 📌 Overview

This project is a Machine Learning-based web application that predicts the quality of tea using key parameters such as temperature, pH, and color score.
It combines **software (ML model + UI)** with a **hardware prototype concept** to simulate real-world usage.

---

## 🎯 Features

* Predicts tea quality instantly
* Simple and user-friendly interface
* Uses Machine Learning for accurate classification
* Clean UI with organic (tea-inspired) design

---

## 🧠 How It Works

The model is trained on a dataset containing tea attributes:

* Temperature
* pH level
* Color score

Based on these inputs, the model classifies tea quality into:

* **0 → Low Quality**
* **1 → Medium Quality**
* **2 → High Quality**

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn

---

## ⚙️ Hardware Component (Prototype)

### 🔌 Components

* Temperature Sensor
* pH Sensor
* Microcontroller (Arduino - simulated)
* Output Display

### 🔄 Working Principle

1. Sensors collect real-time data (temperature, pH).
2. Data is sent to the microcontroller.
3. The processed values are passed to the ML model.
4. The system predicts tea quality and displays the result.

### 🧪 Prototype

The hardware system can be simulated using **Tinkercad**, demonstrating how the model can be applied in real-world tea processing environments.

---

## 📊 Dataset

The dataset contains tea samples with multiple attributes used for training the model.
A large dataset is used to improve prediction accuracy and reliability.

---

## ▶️ How to Run

1. Install required libraries:

```
pip install streamlit pandas scikit-learn
```

2. Run the app:

```
streamlit run app.py
```

---

## 📁 Project Structure

```
├── app.py          # Streamlit UI  
├── main.py         # Machine learning model  
├── tea_data.csv    # Dataset  
└── README.md       # Documentation  
```

---

## 🚀 Future Improvements

* Real-time hardware integration
* Deployment of the web app
* Improved UI/UX design
* More advanced ML models

---

## 👥 Team

Group project developed for academic purposes.

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be used to predict tea quality efficiently and how it can be integrated with hardware systems for real-world applications.

---
