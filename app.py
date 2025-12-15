import streamlit as st
import numpy as np
import pickle
# Load Model & Scaler

model = pickle.load(open("best_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Streamlit Page Config

st.set_page_config(
    page_title="HR Attrition Prediction",
    page_icon="💼",
    layout="centered"
)

# Custom CSS Styling

st.markdown("""
<style>
    .main {
        background: #F4F6F9;
    }
    .title {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #2A4D69;
        padding-bottom: 10px;
    }
    .sub {
        font-size: 18px;
        text-align: center;
        color: #4C657E;
        margin-bottom: 30px;
    }
    .result-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Title & Subtitle

st.markdown("<div class='title'>💼 HR Attrition Prediction</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Predict whether an employee will leave the organization</div>", unsafe_allow_html=True)



