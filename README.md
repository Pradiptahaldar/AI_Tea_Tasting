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
* Humidity
* Aroma
* Color score
---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* numpy
* opencv
* serial
* time

---

## ⚙️ Hardware Component (Prototype)

### 🔌 Components

* Temperature Sensor (DHT11)
* Humidity sensor (DHT11)
* Microcontroller (ESP32 dev module)
* gas sensor (MQ2)

###  Working Principle

1. Sensors collect real-time data (temperature, Aroma, Gas,Humidity).
2. Data is sent to the microcontroller(ESP32).
3. The processed values are passed to the ML model.
4. The system predicts tea quality and displays the result.

###  Prototype

The hardware system can be simulated using **Tinkercad**, demonstrating how the model can be applied in real-world tea processing environments.
its made by us for academic purposes you can buy the things and make it

---

## 📊 Dataset

The dataset contains tea samples with multiple attributes used for training the model.
A large dataset is used to improve prediction accuracy and reliability.

---

## ▶️ How to Run

1. Install required libraries:

```
pip install -r requirements.txt
```

2. Run the app:

```
streamlit run app.py
```


## 📁 Project Structure

```
tea-project/
│
├── main.py
├── app.py
├── pycache
├── tea_dataset.csv
|--requirments .txt
|-- readme.md



```

---

## 🚀 Future Improvements

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
