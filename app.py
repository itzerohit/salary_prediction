import streamlit as st 
import joblib
import numpy as np 

# Title
st.title("💼 Salary Prediction App")

# Divider
st.divider()

# Introduction
st.write("📊 **Welcome!** Use this app to estimate employee salaries based on their experience and job rating at the company.")

# Inputs
years = st.number_input("👨‍💼 Enter the number of years the employee has worked at the company:", value=1, step=1, min_value=0)
jobrate = st.number_input("⭐ Enter the employee's job performance rating (e.g., 1.0 - 5.0):", value=3.5, step=0.5, min_value=0.0)

X = [years, jobrate]

# Load model
model = joblib.load("Linearmodel.pkl")

st.divider()

# Prediction button
predict = st.button("🔮 Predict Salary")

st.divider()

# Output
if predict:
    st.balloons()
    X1 = np.array([X])
    prediction = model.predict(X1)[0]
    
    st.success(f"💰 Estimated Salary: **₹ {prediction:,.2f}**")
    st.caption("This is an approximate prediction based on the input values. Actual salaries may vary.")
else:
    st.info("👆 Please enter the values and press the **Predict Salary** button to get the estimation.")
