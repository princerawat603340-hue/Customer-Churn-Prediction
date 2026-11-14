# Customer Churn Prediction

A Machine Learning-based Customer Churn Prediction application built using **Python, Scikit-learn, Gradient Boosting, and Streamlit**. The application predicts whether a customer is likely to leave a service based on their personal and account-related information.

## 🚀 Live Demo

[Click here to try the application](https://customer-churn-prediction-z4gtkwyjngqdxmhqvfqqrh.streamlit.app/)

## 📌 Project Overview

Customer churn refers to the situation where customers stop using a company's products or services.

This project uses a trained **Gradient Boosting Classifier** to predict customer churn and estimate the probability of a customer leaving the service.

The application provides an interactive interface where users can enter customer details and receive predictions.

## ✨ Features

- Customer churn prediction.
- Churn probability estimation.
- Interactive Streamlit interface.
- Customer information input form.
- Automatic preprocessing through a trained ML pipeline.
- Simple and user-friendly interface.

## 📊 Input Features

The model takes the following 10 features as input:

| Feature | Description |
|---|---|
| CreditScore | Customer's credit score |
| Geography | Customer's country |
| Gender | Customer's gender |
| Age | Customer's age |
| Tenure | Number of years with the company |
| Balance | Customer's account balance |
| NumOfProducts | Number of products used |
| HasCrCard | Whether the customer has a credit card |
| IsActiveMember | Whether the customer is an active member |
| EstimatedSalary | Customer's estimated salary |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Gradient Boosting Classifier
- Pickle
- Streamlit

## ⚙️ Installation and Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/princerawat603340-hue/Customer-Churn-Prediction
   ```

2. Navigate to the project directory:

   ```bash
   cd Customer-Churn-Prediction
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## ⚠️ Dataset Limitation

**Important:** This model is trained on customer data from France, Germany, and Spain.

Therefore, its predictions may not accurately represent customer behaviour in other countries or regions. The model's performance on customers from different geographical locations is not guaranteed.

## 🔮 Future Improvements

- Customer churn analytics dashboard.
- Bulk customer predictions using CSV uploads.
- Customer risk categorization.
- Model performance visualization.
- Additional geographical data for better generalization.

## 👨‍💻 Author

Prince Rawat

---

⭐ If you find this project useful, consider giving the repository a star!
