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
# Preprocess & Predict

if submitted:

    # Encode salary
    salary_map = {"Low": 0, "Medium": 1, "High": 2}
    salary_val = salary_map[salary]

    # Encode binary values
    work_acc = 1 if work_accident == "Yes" else 0
    promo = 1 if promotion_last_5years == "Yes" else 0

    # One-hot encoding for department
    dept_onehot = [1 if d == department else 0 for d in dept_list]

# Combine all inputs
    input_data = np.array([
        satisfaction_level,
        last_evaluation,
        number_project,
        average_montly_hours,
        time_spend_company,
        work_acc,
        promo,
        salary_val
    ] + dept_onehot).reshape(1, -1)

# Scale numeric features
    scaled_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_data)[0]
    probability = model.predict_proba(scaled_data)[0][1]

 # Display Result

    if prediction == 1:
        st.markdown(
            f"""
            <div class='result-box' style='background:#FFE5E5; color:#C0392B;'>
                🚨 <strong>High Attrition Risk!</strong><br>
                Probability: {probability:.2f}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div class='result-box' style='background:#E9F7EF; color:#1D8348;'>
                ✅ <strong>Employee Will Stay</strong><br>
                Probability of Leaving: {probability:.2f}
            </div>
            """, unsafe_allow_html=True)


