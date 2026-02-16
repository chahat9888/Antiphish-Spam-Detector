# app.py code
import streamlit as st
import pickle

# Load saved files
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(page_title="Email Spam Guard", page_icon="📧")
st.title("📧 Phishing & Spam Email Detector")

email_input = st.text_area("Enter text here:", height=200)

if st.button("Predict"):
    if email_input:
        # 1. Clean data (Same as training)
        data = [email_input.lower()]
        # 2. Vectorize
        vectorized_data = vectorizer.transform(data)
        # 3. Predict
        prediction = model.predict(vectorized_data)
        
        if prediction[0] == 1:
            st.error("🚨 Warning:SPAM/PHISHING EMAIL!")
        else:
            st.success("✅ Safe: HAM EMAIL.")
    else:
        st.warning("Enter something.")