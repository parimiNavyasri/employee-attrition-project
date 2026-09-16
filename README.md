\# 👨‍💼 Employee Attrition Prediction \& Explainable HR Analytics



An end-to-end Data Science project that predicts the likelihood of employee attrition using Machine Learning and explains individual predictions using SHAP (SHapley Additive exPlanations).



\## 🚀 Live Demo



👉 \*\*Streamlit App:\*\* https://employee-attrition-project-zenbb3bkadw36vpe4rxlvt.streamlit.app/



The deployed application allows users to enter employee information and receive an attrition prediction, probability estimate, risk category, and an explanation of the factors influencing the prediction.



\---



\## 📌 Project Overview



Employee attrition is an important challenge for organizations because employee turnover can affect productivity, recruitment costs, and workforce planning.



This project uses employee demographic, job, satisfaction, compensation, and work-history information to build a Machine Learning model that estimates whether an employee is likely to leave the organization.



The project also incorporates \*\*SHAP explainability\*\* to understand which features contributed most to each individual prediction.



\---



\## 🎯 Objectives



\* Understand and explore employee attrition data

\* Clean and preprocess the dataset

\* Perform exploratory data analysis

\* Prepare categorical and numerical features for Machine Learning

\* Build and evaluate multiple Machine Learning models

\* Select a primary model based on the project's objective and evaluation results

\* Predict employee attrition probability

\* Explain individual predictions using SHAP

\* Build an interactive Streamlit application

\* Deploy the application online



\---



\## 📊 Dataset



The project uses the \*\*IBM HR Analytics Employee Attrition \& Performance\*\* dataset.



\### Dataset Information



\* \*\*Rows:\*\* 1,470

\* \*\*Original Features:\*\* 35

\* \*\*Target Variable:\*\* `Attrition`

\* \*\*Missing Values:\*\* None

\* \*\*Duplicate Rows:\*\* None



\### Target Distribution



\* \*\*No:\*\* 1,233 employees

\* \*\*Yes:\*\* 237 employees



\### Important Features



The dataset contains information such as:



\* Age

\* Department

\* Job Role

\* Monthly Income

\* Overtime

\* Job Satisfaction

\* Environment Satisfaction

\* Work-Life Balance

\* Total Working Years

\* Years at Company

\* Business Travel

\* Marital Status

\* Education

\* Job Level

\* Number of Companies Worked

\* Years in Current Role

\* Years Since Last Promotion

\* Years With Current Manager



\---



\## 🔄 Machine Learning Workflow



```text

Dataset

&#x20;  ↓

Data Understanding

&#x20;  ↓

Data Cleaning

&#x20;  ↓

Exploratory Data Analysis

&#x20;  ↓

Feature Selection \& Preprocessing

&#x20;  ↓

Train-Test Split

&#x20;  ↓

Model Training

&#x20;  ↓

Model Evaluation

&#x20;  ↓

Logistic Regression Selection

&#x20;  ↓

SHAP Explainability

&#x20;  ↓

Streamlit Application

&#x20;  ↓

Cloud Deployment

```



\---



\## 🤖 Machine Learning Models



The following models were trained and evaluated:



1\. Logistic Regression

2\. Decision Tree

3\. Random Forest

4\. XGBoost



\### Primary Model



\*\*Logistic Regression\*\* was selected as the primary model for the deployed application because the project emphasizes identifying potential attrition cases and the model showed comparatively strong recall, F1-score, and ROC-AUC among the evaluated models.



\### Logistic Regression Test Results



| Metric    |  Score |

| --------- | -----: |

| Accuracy  | 75.17% |

| Precision | 34.88% |

| Recall    | 63.83% |

| F1-Score  | 45.11% |

| ROC-AUC   | 80.11% |



These results are based on the held-out test set and should be interpreted in the context of the dataset's class imbalance.



\---



\## 🔍 Explainable AI with SHAP



To make the Machine Learning predictions more interpretable, this project uses \*\*SHAP (SHapley Additive exPlanations)\*\*.



The Streamlit application provides:



\* Top factors influencing an individual prediction

\* SHAP values

\* Direction of influence

\* SHAP impact visualization



\### Interpretation



\* \*\*Positive SHAP value:\*\* pushes the prediction toward higher attrition risk

\* \*\*Negative SHAP value:\*\* pushes the prediction toward lower attrition risk



SHAP explanations describe how the trained model arrived at a prediction; they should not be interpreted as proof that a particular factor causes employee attrition.



\---



\## 🖥️ Streamlit Application



The deployed application allows users to enter employee information and provides:



\### 🔮 Prediction



\* Employee attrition prediction

\* Estimated attrition probability

\* Risk category



\### 🔍 Explainability



\* Top SHAP-influencing features

\* SHAP values

\* Impact direction

\* SHAP visualization



\### 📌 Additional Information



The application also includes an explanation of the project, technologies used, and an educational-project disclaimer.



\---



\## 🛠️ Technologies Used



\### Programming \& Data



\* Python

\* Pandas

\* NumPy



\### Machine Learning



\* Scikit-learn

\* XGBoost



\### Explainable AI



\* SHAP



\### Deployment \& Application



\* Streamlit

\* Joblib



\### Development



\* Jupyter Notebook

\* Git

\* GitHub



\---



\## 📁 Project Structure



```text

employee-attrition-project/

│

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

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

```



\---



\## ▶️ Run the Project Locally



\### 1. Clone the repository



```bash

git clone https://github.com/parimiNavyasri/employee-attrition-project.git

```



\### 2. Navigate to the project folder



```bash

cd employee-attrition-project

```



\### 3. Install the dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the Streamlit application



```bash

streamlit run app.py

```



The application will open in your browser.



\---



\## 📈 Key Project Outcomes



Through this project, I implemented an end-to-end Machine Learning workflow involving:



\* Data cleaning and validation

\* Exploratory data analysis

\* Feature preprocessing

\* Categorical feature encoding

\* Train-test s



