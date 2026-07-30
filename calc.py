import streamlit as st

if "expression" not in st.session_state:
    st.session_state.expression = ""

st.set_page_config(
    page_title="Satyam Calculator",
    page_icon="logo.png",
    layout="centered"
)

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

st.markdown("---")

display = st.text_input(
    "",
    value="0",
    disabled=True,
    label_visibility="collapsed"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", use_container_width=True)
with col2:
    st.button("8", use_container_width=True)
with col3:
    st.button("9", use_container_width=True)
with col4:
    st.button("÷", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("4", use_container_width=True)
with col2:
    st.button("5", use_container_width=True)
with col3:
    st.button("6", use_container_width=True)
with col4:
    st.button("×", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("1", use_container_width=True)
with col2:
    st.button("2", use_container_width=True)
with col3:
    st.button("3", use_container_width=True)
with col4:
    st.button("-", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("0", use_container_width=True)
with col2:
    st.button(".", use_container_width=True)
with col3:
    st.button("=", use_container_width=True)
with col4:
    st.button("+", use_container_width=True)
