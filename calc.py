import streamlit as st

st.set_page_config(
    page_title="Satyam Calculator",
    page_icon="logo.png",
    layout="centered"
)

st.image("logo.png", width=150)
st.title("🧮 SATYAM CALCULATOR")

num1 = st.number_input("Pahli Rashi", value=0.0)
op = st.selectbox("Operator", ["+", "-", "*", "/"])
num2 = st.number_input("Dushri Rashi", value=0.0)

if st.button("Calculate"):
    if op == "+":
        st.success(num1 + num2)
    elif op == "-":
        st.success(num1 - num2)
    elif op == "*":
        st.success(num1 * num2)
    elif op == "/":
        if num2 != 0:
            st.success(num1 / num2)
        else:
            st.error("Zero se Divide Nahi Hota!")
