#Project 01: Unit Convertor
#Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st  # type: ignore



st.markdown("""
<style>
body {
    background-color:rgb(174, 185, 206);
    color: #000000;
}
.stApp {
    background-color: #f0f2f6;
    color: #000000;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
h1 {
    color: #000000;
    text-align: center;
}
.stButton>button {
    background-color: #000000;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #000000;
    color: #ffffff;
}
.result-box {
    background-color: #000000;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    font-size: 16px;
}
.footer{
    text-align: center;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<h1>Unit Convertor By Muhib Anwar</h1>", unsafe_allow_html=True)
st.write("---")

# Define conversion factors to meters
conversion_factors = {
    "Meters": 1,
    "Kilometers": 1000,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254
}

# Sidebar for input
st.sidebar.header("Input")
value = st.sidebar.number_input("Enter the value", min_value=0.0, step=0.1)

# Main content area
col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From Unit", list(conversion_factors.keys()))
with col2:
    to_unit = st.selectbox("To Unit", list(conversion_factors.keys()))

# Conversion logic
if value is not None:
    # Convert to meters first (base unit)
    meters = value * conversion_factors[from_unit]
    # Convert from meters to target unit
    result = meters / conversion_factors[to_unit]
    
    # Display result
    st.success(f"Result: {value} {from_unit} = {result:.6f} {to_unit}")

    st.markdown("<div class='footer'>Developed by Muhib Anwar</div>", unsafe_allow_html=True)
      