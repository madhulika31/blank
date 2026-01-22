import streamlit as st
import pickle
from datetime import date, timedelta

# -------- Load Model --------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🛂 Visa Processing Time Prediction (Linear Regression)")

# -------- Inputs --------
name = st.text_input("Applicant Name")

country = st.selectbox("Country", ["USA", "UK", "Canada", "Australia"])
visa_type = st.selectbox("Visa Type", ["Student", "Work"])
application_date = st.date_input("Application Date", value=date.today())

# -------- Encoding --------
country_map = {"USA": 1, "UK": 2, "Canada": 3, "Australia": 4}
visa_map = {"Student": 1, "Work": 2}

# -------- Predict --------
if st.button("Predict"):

    if name.strip() == "":
        st.warning("Please enter name")
    else:
        c = country_map[country]
        v = visa_map[visa_type]

        days = int(model.predict([[c, v]])[0])
        decision_date = application_date + timedelta(days=days)

        st.success("Prediction Successful ✅")
        st.write("Applicant:", name)
        st.write("Estimated Processing Days:", days)
        st.write("Expected Decision Date:", decision_date.strftime("%d-%m-%Y"))
