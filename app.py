import streamlit as st
import pickle

try:
    model = pickle.load(open("model.pkl", "rb"))
except Exception as e:
    st.error(f"Model loading failed: {e}")