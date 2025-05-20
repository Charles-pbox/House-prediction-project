# app.py
import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App Title
st.title("🏠 House Price Prediction App")

st.markdown("Enter the details below to estimate the house price:")

# Numeric Inputs
area = st.number_input("Area (sq ft)", min_value=0)
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
bathroom = st.number_input("Number of Bathrooms", min_value=0)
stories = st.number_input("Number of Stories", min_value=0)
parking = st.number_input("Number of Parking Spaces", min_value=0)

# Function to convert Yes/No to binary
def map_yes_no(value):
    return 1 if value == "Yes" else 0

# Categorical Inputs (Yes/No selections)
mainroad = st.selectbox("Access to Main Road?", ["Yes", "No"])
guestroom = st.selectbox("Guest Room Available?", ["Yes", "No"])
basement = st.selectbox("Basement Present?", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating?", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning?", ["Yes", "No"])
prefarea = st.selectbox("In Preferred Area?", ["Yes", "No"])

# Convert categorical inputs
mainroad_val = map_yes_no(mainroad)
guestroom_val = map_yes_no(guestroom)
basement_val = map_yes_no(basement)
hotwaterheating_val = map_yes_no(hotwaterheating)
airconditioning_val = map_yes_no(airconditioning)
prefarea_val = map_yes_no(prefarea)

# Arrange input in the expected order
input_data = np.array([[
    area, bedrooms, bathroom, stories, parking,
    mainroad_val, guestroom_val, basement_val,
    hotwaterheating_val, airconditioning_val, prefarea_val
]])

# Predict when button clicked
if st.button("Predict House Price"):
    prediction = model.predict(input_data)
    st.success(f"💵 Estimated House Price: ${prediction[0]:,.2f}")
