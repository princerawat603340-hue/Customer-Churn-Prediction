import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open("churn_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict whether the customer is likely to churn.")
st.info(
    "Note: This model is trained on customer data from France, Germany, "
    "and Spain. Predictions for customers from other countries may not "
    "be equally accurate."
)

# Input form
with st.form("customer_form"):

    st.subheader("Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=650
        )

        geography = st.selectbox(
            "Geography",
            ["France", "Germany", "Spain"]
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        tenure = st.number_input(
            "Tenure",
            min_value=0,
            max_value=10,
            value=5
        )

    with col2:
        balance = st.number_input(
            "Balance",
            min_value=0.0,
            value=50000.0
        )

        num_products = st.number_input(
            "Number of Products",
            min_value=1,
            max_value=4,
            value=2
        )

        has_cr_card = st.selectbox(
            "Has Credit Card?",
            ["Yes", "No"]
        )

        is_active_member = st.selectbox(
            "Is Active Member?",
            ["Yes", "No"]
        )

        estimated_salary = st.number_input(
            "Estimated Salary",
            min_value=0.0,
            value=50000.0
        )

    submitted = st.form_submit_button(
        "Predict Churn",
        use_container_width=True
    )

# Prediction after submission
if submitted:

    input_data = pd.DataFrame([{
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": 1 if has_cr_card == "Yes" else 0,
        "IsActiveMember": 1 if is_active_member == "Yes" else 0,
        "EstimatedSalary": estimated_salary
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Customer is likely to churn!")
    else:
        st.success("Customer is likely to stay!")

    st.metric("Churn Probability", f"{probability * 100:.2f}%")
