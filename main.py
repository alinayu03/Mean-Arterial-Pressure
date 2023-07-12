import streamlit as st

st.title("Mean Arterial Pressure (MAP) Calculator")

# Input fields for SBP and DBP
st.header("Enter the values:")
SBP = st.number_input('Systolic Blood Pressure (mmHg)',
                      min_value=0, max_value=300, value=120)
DBP = st.number_input('Diastolic Blood Pressure (mmHg)',
                      min_value=0, max_value=200, value=80)

# Calculation
MAP = DBP + (1/3) * (SBP - DBP)

# Display the result
st.header("Result:")
st.write(f"The Mean Arterial Pressure (MAP) is {MAP:.2f} mmHg")
