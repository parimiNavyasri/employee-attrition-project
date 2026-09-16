import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent

# Load trained model
model = joblib.load(
    BASE_DIR / "models" / "logistic_regression_model.pkl"
)

# Load preprocessing pipeline
preprocessor = joblib.load(
    BASE_DIR / "models" / "preprocessor.pkl"
)

# Load SHAP explainer
explainer = joblib.load(
    BASE_DIR / "models" / "shap_explainer.pkl"
)

# Page configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="👨‍💼",
    layout="wide"
)

# Title
st.title("👨‍💼 Employee Attrition Prediction System")

st.write(
    "Enter employee information below to predict the likelihood of employee attrition."
)

st.divider()

# Employee Information
st.header("📋 Employee Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        value=30
    )

    business_travel = st.selectbox(
        "Business Travel",
        ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    )

with col2:
    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        max_value=1500,
        value=800
    )

    department = st.selectbox(
        "Department",
        ["Sales", "Research & Development", "Human Resources"]
    )

with col3:
    distance_from_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

    education = st.number_input(
        "Education Level",
        min_value=1,
        max_value=5,
        value=3
    )

st.divider()

# Additional Employee Information
st.header("💼 Job & Employee Details")

col1, col2, col3 = st.columns(3)

with col1:
    education_field = st.selectbox(
        "Education Field",
        [
            "Life Sciences",
            "Medical",
            "Marketing",
            "Technical Degree",
            "Human Resources",
            "Other"
        ]
    )

    environment_satisfaction = st.number_input(
        "Environment Satisfaction",
        min_value=1,
        max_value=4,
        value=3
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=30,
        max_value=100,
        value=65
    )

with col3:
    job_involvement = st.number_input(
        "Job Involvement",
        min_value=1,
        max_value=4,
        value=3
    )

    job_level = st.number_input(
        "Job Level",
        min_value=1,
        max_value=5,
        value=2
    )
st.divider()

# Work and Career Details
st.header("📈 Work & Career Details")

col1, col2, col3 = st.columns(3)

with col1:
    job_role = st.selectbox(
        "Job Role",
        [
            "Sales Executive",
            "Research Scientist",
            "Laboratory Technician",
            "Manufacturing Director",
            "Healthcare Representative",
            "Manager",
            "Sales Representative",
            "Research Director",
            "Human Resources"
        ]
    )

    job_satisfaction = st.number_input(
        "Job Satisfaction",
        min_value=1,
        max_value=4,
        value=3
    )

with col2:
    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced"]
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=20000,
        value=5000
    )

with col3:
    monthly_rate = st.number_input(
        "Monthly Rate",
        min_value=2000,
        max_value=27000,
        value=14000
    )

    num_companies_worked = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        max_value=9,
        value=2
    )
st.divider()

# Work Experience and Compensation
st.header("💰 Experience & Compensation")

col1, col2, col3 = st.columns(3)

with col1:
    over_time = st.selectbox(
        "Over Time",
        ["Yes", "No"]
    )

    percent_salary_hike = st.number_input(
        "Percent Salary Hike",
        min_value=11,
        max_value=25,
        value=15
    )

with col2:
    performance_rating = st.number_input(
        "Performance Rating",
        min_value=1,
        max_value=4,
        value=3
    )

    relationship_satisfaction = st.number_input(
        "Relationship Satisfaction",
        min_value=1,
        max_value=4,
        value=3
    )

with col3:
    stock_option_level = st.number_input(
        "Stock Option Level",
        min_value=0,
        max_value=3,
        value=1
    )

    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=8
    )
st.divider()

# Employee History and Satisfaction
st.header("📊 Employee History & Satisfaction")

col1, col2, col3 = st.columns(3)

with col1:
    training_times_last_year = st.number_input(
        "Training Times Last Year",
        min_value=0,
        max_value=6,
        value=3
    )

    work_life_balance = st.number_input(
        "Work Life Balance",
        min_value=1,
        max_value=4,
        value=3
    )

with col2:
    years_at_company = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=40,
        value=5
    )

    years_in_current_role = st.number_input(
        "Years in Current Role",
        min_value=0,
        max_value=18,
        value=3
    )

with col3:
    years_since_last_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        max_value=15,
        value=2
    )

    years_with_curr_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=17,
        value=3
    )
st.divider()
# Prediction Section
st.header("🔮 Attrition Prediction")

if st.button("Predict Attrition", type="primary"):

    # Create employee data
    employee_data = pd.DataFrame({
        "Age": [age],
        "BusinessTravel": [business_travel],
        "DailyRate": [daily_rate],
        "Department": [department],
        "DistanceFromHome": [distance_from_home],
        "Education": [education],
        "EducationField": [education_field],
        "EnvironmentSatisfaction": [environment_satisfaction],
        "Gender": [gender],
        "HourlyRate": [hourly_rate],
        "JobInvolvement": [job_involvement],
        "JobLevel": [job_level],
        "JobRole": [job_role],
        "JobSatisfaction": [job_satisfaction],
        "MaritalStatus": [marital_status],
        "MonthlyIncome": [monthly_income],
        "MonthlyRate": [monthly_rate],
        "NumCompaniesWorked": [num_companies_worked],
        "OverTime": [over_time],
        "PercentSalaryHike": [percent_salary_hike],
        "PerformanceRating": [performance_rating],
        "RelationshipSatisfaction": [relationship_satisfaction],
        "StockOptionLevel": [stock_option_level],
        "TotalWorkingYears": [total_working_years],
        "TrainingTimesLastYear": [training_times_last_year],
        "WorkLifeBalance": [work_life_balance],
        "YearsAtCompany": [years_at_company],
        "YearsInCurrentRole": [years_in_current_role],
        "YearsSinceLastPromotion": [years_since_last_promotion],
        "YearsWithCurrManager": [years_with_curr_manager]
    })

    # Apply preprocessing
    employee_processed = preprocessor.transform(employee_data)

    # Make prediction
    prediction = model.predict(employee_processed)[0]

    # Get probability
    probability = model.predict_proba(employee_processed)[0][1]

    # Convert probability to percentage
    probability_percentage = probability * 100

    # Risk category
    if probability_percentage >= 70:
        risk_level = "High Risk"
    elif probability_percentage >= 40:
        risk_level = "Medium Risk"
    else:
        risk_level = "Low Risk"

    # Display prediction
    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("⚠️ Prediction: Employee is likely to leave")
    else:
        st.success("✅ Prediction: Employee is likely to stay")

    # Display probability and risk
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Attrition Probability",
            f"{probability_percentage:.2f}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk_level
        )

    # Progress bar
    st.write("Attrition Probability")
    st.progress(float(probability))

    # Explanation
    st.info(
        "This probability represents the model's estimated likelihood "
        "of attrition based on the employee information provided. "
        "It should be treated as a model estimate, not a certainty."
    )

    # SHAP Explanation
    st.subheader("🔍 Why did the model make this prediction?")

    # Calculate SHAP values for this employee
    employee_shap = explainer(employee_processed)

    # Get SHAP values
    shap_values_employee = employee_shap.values[0]

    # Get processed feature names
    shap_feature_names = preprocessor.get_feature_names_out()

    # Create SHAP dataframe
    shap_df = pd.DataFrame({
        "Feature": shap_feature_names,
        "SHAP Value": shap_values_employee
    })

    # Calculate absolute impact
    shap_df["Absolute Impact"] = shap_df["SHAP Value"].abs()

    # Sort by strongest impact
    shap_df = shap_df.sort_values(
        by="Absolute Impact",
        ascending=False
    )

    # Take top 10 factors
    top_10_shap = shap_df.head(10).copy()

    # Make feature names easier to understand
    top_10_shap["Feature"] = (
        top_10_shap["Feature"]
        .str.replace("categorical__", "", regex=False)
        .str.replace("remainder__", "", regex=False)
    )

    # Create impact description
    top_10_shap["Impact"] = top_10_shap["SHAP Value"].apply(
        lambda x: "Increases attrition risk" if x > 0
        else "Decreases attrition risk"
    )

    # Display explanation
    st.write("The following factors had the strongest influence on this prediction:")

    st.dataframe(
        top_10_shap[
            ["Feature", "SHAP Value", "Impact"]
        ],
        use_container_width=True
    )

    st.caption(
        "Positive SHAP values increase the model's predicted attrition risk, "
        "while negative SHAP values decrease it."
    )

    # SHAP Impact Visualization
    st.subheader("📈 SHAP Impact Visualization")

    # Prepare chart data
    chart_df = top_10_shap.sort_values(
        by="SHAP Value",
        ascending=True
    )

    # Create horizontal bar chart
    st.bar_chart(
        chart_df.set_index("Feature")["SHAP Value"]
    )

    st.caption(
        "Bars to the right of zero indicate factors that increase "
        "predicted attrition risk. Bars to the left indicate factors "
        "that decrease predicted attrition risk."
    )

    # About the Project
st.divider()

st.header("📌 About This Project")

st.write(
    """
    This Employee Attrition Prediction System uses Machine Learning
    to estimate the likelihood of employee attrition based on
    employee demographics, job characteristics, satisfaction,
    compensation, and work history.

    The application uses Logistic Regression as the primary prediction
    model and SHAP (SHapley Additive exPlanations) to explain which
    employee factors influenced each prediction.
    """
)

st.subheader("🛠️ Technologies Used")

st.write(
    "Python • Pandas • NumPy • Scikit-learn • SHAP • Streamlit"
)

st.subheader("⚠️ Disclaimer")

st.info(
    "This application is an educational Data Science project. "
    "Predictions are model estimates based on historical data and "
    "should not be treated as certain outcomes or as the sole basis "
    "for employment-related decisions."
)
     
