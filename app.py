import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the model
model = joblib.load('insurance_model.pkl')

st.set_page_config(
    page_title="Insurance Cost Prediction",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("💰 Insurance Cost Prediction")
st.write("This application predicts your insurance cost based on your inputs.")

# Define unique values for categorical features (ensure these match your training data)
# These values should ideally come from the original training process or be explicitly defined.
unique_sex = ['female', 'male']
unique_smoker = ['yes', 'no']
unique_region = ['southwest', 'southeast', 'northwest', 'northeast']

# Initialize and fit LabelEncoders for app.py (must be consistent with training)
sex_encoder_app = LabelEncoder()
sex_encoder_app.fit(unique_sex)

smoker_encoder_app = LabelEncoder()
smoker_encoder_app.fit(unique_smoker)

region_encoder_app = LabelEncoder()
region_encoder_app.fit(unique_region)

st.header("Please provide your details:")

with st.form("prediction_form"):
    age = st.slider("Age", 18, 64, 30)
    sex = st.selectbox("Sex", unique_sex)
    bmi = st.number_input("BMI", min_value=15.0, max_value=55.0, value=25.0, step=0.1)
    children = st.slider("Number of Children", 0, 5, 0)
    smoker = st.selectbox("Smoker", unique_smoker)
    region = st.selectbox("Region", unique_region)

    submitted = st.form_submit_button("Predict Insurance Cost")

    if submitted:
        # Encode categorical features
        encoded_sex = sex_encoder_app.transform([sex])[0]
        encoded_smoker = smoker_encoder_app.transform([smoker])[0]
        encoded_region = region_encoder_app.transform([region])[0]

        # Create a DataFrame for prediction
        new_data = pd.DataFrame({
            "age": [age],
            "sex": [encoded_sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [encoded_smoker],
            "region": [encoded_region]
        })

        # Make prediction
        prediction = model.predict(new_data)[0]

        st.success(f"Predicted Insurance Cost: **${prediction:.2f}**")

st.markdown("""
    ---
    *Note: This is a simplified prediction based on a trained model.
    Results may vary depending on the model's accuracy and the data it was trained on.*
    """)