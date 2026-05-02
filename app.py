import streamlit as st
import joblib
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

try:
    model = joblib.load("resume_classifier.pkl")
except Exception as e:
    st.error(f"Model loading failed: {e}")

st.title("Resume Classification App")

user_input = st.text_area("Paste your resume text")

if st.button("Predict"):
    if user_input:
        prediction = model.predict([user_input])
        st.success(f"Predicted Category: {prediction[0]}")
    else:
        st.warning("Please enter resume text")