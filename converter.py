import streamlit as st

# Custom CSS
st.markdown(""" 
    <style>
    .stApp {
        background: linear-gradient(135deg,rgb(182, 196, 247),rgb(111, 115, 184));
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        font-size: 36px;
        font-weight: 700;
        color:rgb(255, 255, 255) !important;
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(75deg,rgb(215, 215, 251),rgb(181, 194, 251));
        color: #fff;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.4);
        border: none;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg,rgb(206, 207, 209),rgb(229, 230, 238));
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.5);
        color: #000;
        font-weight: 600;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(144, 100, 227, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #000;
        font-size: 14px;
    }
    /* Change Sidebar Background */
    [data-testid="stSidebar"] {
       background: linear-gradient(135deg,rgb(182, 196, 247),rgb(111, 115, 184));
    }

    /* Style the Dropdown (Select Box) */
    [data-testid="stSidebar"] select {
        background-color: #00b09b !important; /* Green Background */
        color: white !important; /* White Text */
        border-radius: 8px;
        padding: 8px;
        font-size: 16px;
        font-weight: bold;
    }

    /* Change Dropdown Hover Effect */
    [data-testid="stSidebar"] select:hover {
        background-color: #009688 !important; /* Darker Green */
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀Unit Converter")
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox(
    "Choose Conversion Type", ["Length", "Weight", "Temperature"]
)
value = st.number_input("Enter Value", value=0.0, min_value=None, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox(
            "From",
            ["Meter", "Kilometer", "Centimeters", "Millimeters", "Miles", "Yards", "Inch", "Feet"],
        )
    with col2:
        to_unit = st.selectbox(
            "To",
            ["Meter", "Kilometer", "Centimeters", "Millimeters", "Miles", "Yards", "Inch", "Feet"],
        )

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Gram", "Milligram", "Pounds", "Ounce"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28,
        "Inch": 39.37,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1000000,
        "Pounds": 2.2046,
        "Ounce": 35.27,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9 / 5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5 / 9) if to_unit == "Celsius" else ((value - 32) * 5 / 9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9 / 5 + 32) if to_unit == "Fahrenheit" else value
    return value


# Button for conversion
if st.button("🤖 Convert"):
    result = None
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    if result is not None:
        st.markdown(
            f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>",
            unsafe_allow_html=True,
        )

st.markdown("<div class='footer'>Created with ❤️ by Saima Salar</div>", unsafe_allow_html=True)
