"""Entrypoint for app. Defines navigation."""

import streamlit as st

# Initialise session state before running any page
if "scenarios" not in st.session_state:
    st.session_state.scenarios = {}

pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
    ]
)

pg.run()
