import streamlit as st

pg = st.navigation(
    pages=[
        st.Page("page1.py"),
        st.Page("page2.py"),
    ],
    position="top",
)
pg.run()
