import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Resume Classification App")

user_input = st.text_area("Paste your resume text here")

if st.button("Predict"):
    if user_input:
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)
        st.success(f"Predicted Category: {prediction[0]}")
    else:
        st.warning("Please enter resume text")