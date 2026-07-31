import streamlit as st
from calculator import press, clear, backspace, calculate

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Satyam Calculator",
    page_icon="logo.png",
    layout="centered"
)

# ---------------- CSS ----------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "expression" not in st.session_state:
    st.session_state.expression = ""
    
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- HEADER ----------------
col1, col2 = st.columns([1,4])

with col1:
    st.image("logo.png", width=85)

with col2:
    st.markdown("""
    <h1 style="margin-bottom:0;">SATYAM CALCULATOR</h1>
    <p style="color:gray;margin-top:-10px;">
    SMART • POWERFUL • ACCURATE
    </p>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- DISPLAY ----------------
st.markdown(
    f"""
    <div class="display">
        <span>{st.session_state.expression if st.session_state.expression else "0"}</span>
    </div>
    """,
    unsafe_allow_html=True,
)
# ---------------- ROW 1 ----------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("AC", use_container_width=True):
        st.session_state.expression = clear()
        st.rerun()

with c2:
    if st.button("⌫", use_container_width=True):
        st.session_state.expression = backspace(st.session_state.expression)
        st.rerun()

with c3:
    if st.button("%", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "%")
        st.rerun()

with c4:
    if st.button("÷", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "÷")
        st.rerun()

# ---------------- ROW 2 ----------------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["7", "8", "9"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(
                st.session_state.expression, value
            )
            st.rerun()

with c4:
    if st.button("×", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "×")
        st.rerun()
        # ---------------- ROW 3 ----------------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["4", "5", "6"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(
                st.session_state.expression, value
            )
            st.rerun()

with c4:
    if st.button("-", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "-")
        st.rerun()

# ---------------- ROW 4 ----------------
c1, c2, c3, c4 = st.columns(4)

for col, value in zip([c1, c2, c3], ["1", "2", "3"]):
    with col:
        if st.button(value, use_container_width=True):
            st.session_state.expression = press(
                st.session_state.expression, value
            )
            st.rerun()

with c4:
    if st.button("+", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "+")
        st.rerun()

# ---------------- ROW 5 ----------------
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("0", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, "0")
        st.rerun()

with c2:
    if st.button(".", use_container_width=True):
        st.session_state.expression = press(st.session_state.expression, ".")
        st.rerun()

with c3:
    if st.button("=", use_container_width=True):
        st.session_state.expression = calculate(st.session_state.expression)
        st.rerun()
