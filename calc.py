import streamlit as st
from calculator import press, clear, backspace, calculate

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Satyam Calculator",
    page_icon="logo.png",
    layout="centered"
)

if "expression" not in st.session_state:
    st.session_state.expression = ""

# ---------- HEADER ----------
col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.png", width=90)

with col2:
    st.markdown("""
    <h1 style="margin-bottom:0;">SATYAM CALCULATOR</h1>
    <p style="color:gray;margin-top:-10px;">
    SMART • POWERFUL • ACCURATE
    </p>
    """, unsafe_allow_html=True)

st.divider()

# ---------- DISPLAY ----------
st.text_input(
    "",
    value=st.session_state.expression,
    disabled=True,
    label_visibility="collapsed"
)

# ---------- ROW 1 ----------
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("AC", use_container_width=True):
        st.session_state.expression = clear()

with c2:
    if st.button("⌫", use_container_width=True):
        st.session_state.expression = backspace(st.session_state.expression)

with c3:
    if st.button("%", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "%")

with c4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "÷")

# ---------- ROW 2 ----------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["7", "8", "9"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(st.session_state.expression, value)

with c4:
    if st.button("×", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "×")

# ---------- ROW 3 ----------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["4", "5", "6"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(st.session_state.expression, value)

with c4:
    if st.button("-", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "-")

# ---------- ROW 4 ----------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["1", "2", "3"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(st.session_state.expression, value)

with c4:
    if st.button("+", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "+")

# ---------- ROW 5 ----------
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("0", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "0")

with c2:
    if st.button(".", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, ".")

with c3:
    if st.button("=", use_container_width=True):
        st.session_state.expression = calculate(st.session_state.expression)