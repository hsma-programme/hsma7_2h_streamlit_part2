import streamlit as st

with st.popover("Open popover"):
    st.write("Hello!")

st.write("""
This is our demo app.

We are demonstrating `st.popover`.

It will appear over the top of this text when clicked.
""")