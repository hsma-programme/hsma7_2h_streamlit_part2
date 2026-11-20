import streamlit as st

with st.sidebar:
    st.header("Theme demo")

st.header("Text")

st.write("This is normal text, with **bold** and *italic* examples.")

st.code('st.write("Code uses a separate font.")', language="python")

st.header("Input widgets")

st.text_input("Scenario name", value="Baseline")
st.slider("Number of replications", min_value=1, max_value=100, value=30)

st.header("Buttons")

st.button("Primary button", type="primary")
st.button("Secondary button")

