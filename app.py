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

# Form Layout

with st.form("input_form"):
    st.write("### 🧑‍💻 Employee Information")
    
    col1, col2 = st.columns(2)

    with col1:
        satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
        last_evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.6)
        number_project = st.number_input("Number of Projects", 1, 10, 3)
        salary = st.selectbox("Salary Level", ["Low", "Medium", "High"])

    with col2:
        average_montly_hours = st.number_input("Average Monthly Hours", 40, 300, 150)
        time_spend_company = st.number_input("Years in Company", 1, 12, 3)
        work_accident = st.selectbox("Had Work Accident?", ["No", "Yes"])
        promotion_last_5years = st.selectbox("Promoted in Last 5 Years?", ["No", "Yes"])

    st.write("### 🏢 Department Details")
    dept_list = [
        "IT", "RandD", "accounting", "hr", "management",
        "marketing", "product_mng", "sales", "support", "technical"
    ]
    department = st.selectbox("Department", dept_list)

    submitted = st.form_submit_button("🔍 Predict Attrition")


