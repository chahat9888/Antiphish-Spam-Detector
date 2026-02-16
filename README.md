# 🛡️ Antiphish-Spam Email Detector (Machine Learning)

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg)

An AI-powered web application that detects whether an email or message is **Spam (Phishing)** or **Ham (Safe)**. This project uses a **Linear SVM (Support Vector Machine)** model trained on a hybrid dataset to provide high accuracy in real-time.



## 🚀 Features
- **Hybrid Data:** Trained on two diverse datasets (SMS Spam Collection & Enron Email Dataset) for better generalization.
- **High Accuracy:** Achieved ~96.5% accuracy using Linear SVC.
- **Interactive UI:** A clean, minimal dashboard built with Streamlit.
- **Robust Preprocessing:** Handles noise, punctuation, and case sensitivity using NLP techniques.

## 🛠️ Tech Stack
- **Language:** Python
- **Machine Learning:** Scikit-learn (LinearSVC)
- **Natural Language Processing:** TF-IDF Vectorizer
- **Frontend:** Streamlit
- **Data Analysis:** Pandas, Numpy

## 📂 Project Structure
```text
├── app.py              # Streamlit frontend code
├── model.pkl           # Trained Linear SVM model
├── vectorizer.pkl      # Saved TF-IDF Vectorizer
├── requirements.txt    # List of dependencies for deployment
├── README.md           # Project documentation
└── train.py            # (Optional) Model training script
