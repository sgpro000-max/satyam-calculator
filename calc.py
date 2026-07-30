import streamlit as st

st.set_page_config(
    page_title="Satyam Calculator",
    page_icon="logo.png",
    layout="centered"
)

col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=100)

with col2:
    st.markdown("""
    <h1 style="margin-bottom:0;">SATYAM CALCULATOR</h1>
    <p style="color:#00e5ff;margin-top:0;">
    SMART • POWERFUL • ACCURATE
    </p>
    """, unsafe_allow_html=True)

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
