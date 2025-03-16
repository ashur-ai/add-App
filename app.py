import streamlit as st

# Streamlit app title
st.title("Simple Addition App")

# User input for two numbers
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# Button to add numbers
if st.button("Add"):
    result = num1 + num2
    st.success(f"The sum is: {result}")
