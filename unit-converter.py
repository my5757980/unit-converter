# unit-converter-streamlit.py
import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="Ruler", layout="centered")
st.title("Unit Converter (1991–2025)")
st.markdown("---")

# ================================
# MAIN MENU
# ================================
converters = {
    'Length': 'Length Converter',
    'Weight': 'Weight Converter',
    'Temperature': 'Temperature Converter',
    'Time': 'Time Converter',
    'Speed': 'Speed Converter',
    'Area': 'Area Converter',
    'Volume': 'Volume Converter'
}

choice = st.selectbox("Choose a category:", list(converters.keys()))

# ================================
# LENGTH
# ================================
if choice == 'Length':
    st.subheader("Length Converter")
    units = {
        'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100,
        'Millimeter': 1000, 'Mile': 0.000621371, 'Foot': 3.28084, 'Inch': 39.3701
    }
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="l1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="l2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="l3")
    if st.button("Convert", key="l4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

# ================================
# WEIGHT
# ================================
elif choice == 'Weight':
    st.subheader("Weight Converter")
    units = {'Kilogram': 1, 'Gram': 1000, 'Milligram': 1_000_000, 'Pound': 2.20462, 'Ounce': 35.274}
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="w1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="w2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="w3")
    if st.button("Convert", key="w4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

# ================================
# TEMPERATURE
# ================================
elif choice == 'Temperature':
    st.subheader("Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_temp = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"], key="t1")
    with col2:
        to_temp = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"], key="t2")
    value = st.number_input("Enter value:", value=0.0, key="t3")
    if st.button("Convert", key="t4"):
        if from_temp == "Celsius":
            c = value
        elif from_temp == "Fahrenheit":
            c = (value - 32) * 5/9
        else:
            c = value - 273.15
        if to_temp == "Celsius":
            result = c
        elif to_temp == "Fahrenheit":
            result = c * 9/5 + 32
        else:
            result = c + 273.15
        st.success(f"**{value}° {from_temp} = {result:.2f}° {to_temp}**")

# ================================
# TIME
# ================================
elif choice == 'Time':
    st.subheader("Time Converter")
    units = {'Second': 1, 'Minute': 1/60, 'Hour': 1/3600, 'Day': 1/86400, 'Week': 1/604800}
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="ti1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="ti2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="ti3")
    if st.button("Convert", key="ti4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

# ================================
# SPEED
# ================================
elif choice == 'Speed':
    st.subheader("Speed Converter")
    units = {'m/s': 1, 'km/h': 3.6, 'mph': 2.23694, 'knot': 1.94384}
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="s1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="s2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="s3")
    if st.button("Convert", key="s4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

# ================================
# AREA
# ================================
elif choice == 'Area':
    st.subheader("Area Converter")
    units = {
        'Square Meter': 1, 'Square Kilometer': 1e-6, 'Square Foot': 10.7639,
        'Square Yard': 1.19599, 'Acre': 0.000247105, 'Hectare': 0.0001
    }
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="a1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="a2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="a3")
    if st.button("Convert", key="a4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

# ================================
# VOLUME
# ================================
elif choice == 'Volume':
    st.subheader("Volume Converter")
    units = {'Liter': 1, 'Milliliter': 1000, 'Cubic Meter': 0.001, 'Gallon (US)': 0.264172, 'Cup': 4.22675}
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", list(units.keys()), key="v1")
    with col2:
        to_unit = st.selectbox("To", list(units.keys()), key="v2")
    value = st.number_input("Enter value:", min_value=0.0, value=1.0, key="v3")
    if st.button("Convert", key="v4"):
        result = value * units[from_unit] / units[to_unit]
        st.success(f"**{value} {from_unit} = {result:.6f} {to_unit}**")

st.markdown("---")
st.caption("Made with Streamlit | By Grok (1991–2025)")