\# Employee Attrition Prediction \& Explainable HR Analytics



\## 📌 Project Overview



Employee attrition is an important challenge for organizations because employee turnover can affect productivity, recruitment costs, and workforce planning.



This project uses Machine Learning to predict whether an employee is likely to leave the organization based on factors such as job role, overtime, income, satisfaction, experience, work-life balance, and other employee-related characteristics.



The project also uses SHAP (SHapley Additive exPlanations) to explain which factors influenced an individual prediction.



\## 🎯 Project Objectives



\- Analyze employee data and identify patterns related to attrition.

\- Perform data cleaning and preprocessing.

\- Build and compare multiple Machine Learning models.

\- Predict the likelihood of employee attrition.

\- Explain individual predictions using SHAP.

\- Build an interactive Streamlit web application.

\- Deploy the application for practical demonstration.



\## 📊 Dataset



The project uses the IBM HR Analytics Employee Attrition \& Performance dataset.



The dataset contains information about employees, including:



\- Age

\- Department

\- Job Role

\- Monthly Income

\- Overtime

\- Job Satisfaction

\- Environment Satisfaction

\- Work-Life Balance

\- Total Working Years

\- Years at Company

\- Business Travel

\- Marital Status

\- Education

\- And other employee-related attributes



The target variable is:



\*\*Attrition\*\*

\- Yes — Employee left the organization

\- No — Employee stayed with the organization



\## 🤖 Machine Learning Models



The following models were evaluated:



1\. Logistic Regression

2\. Decision Tree

3\. Random Forest

4\. XGBoost



Logistic Regression was selected as the primary model for the Streamlit application because the project places emphasis on identifying potential attrition cases and its evaluation showed comparatively strong recall and ROC-AUC on the held-out test set.



\## 🔍 Explainable AI with SHAP



SHAP is used to explain individual predictions.



The application displays:



\- Top factors influencing the prediction

\- SHAP values

\- Whether each factor increases or decreases the model's predicted attrition risk

\- A SHAP impact visualization



Positive SHAP values indicate that a feature pushes the model toward higher predicted attrition risk, while negative values push the prediction toward lower predicted attrition risk.



\## 🖥️ Streamlit Application



The Streamlit application allows users to enter employee information and receive:



\- Attrition prediction

\- Attrition probability

\- Risk category

\- Top SHAP factors

\- SHAP impact visualization



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- XGBoost

\- SHAP

\- Joblib

\- Streamlit

\- Jupyter Notebook



\## 📁 Project Structure



```text

employee-attrition-project/

│

├── app.py

├── requirements.txt

├── .gitignore

├── README.md

│

├── data/

│   └── WA\_Fn-UseC\_-HR-Employee-Attrition.csv

│

├── models/

│   ├── logistic\_regression\_model.pkl

│   ├── preprocessor.pkl

│   └── shap\_explainer.pkl

│

└── notebooks/

&#x20;   └── 01\_data\_understanding.ipynb

