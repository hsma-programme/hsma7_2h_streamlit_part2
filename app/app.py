"""Entrypoint for app. Configures app and defines navigation."""

import streamlit as st

# Initialise session state before running any page
if "scenarios" not in st.session_state:
    st.session_state.scenarios = {}

# Define pages and their order
pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
        st.Page("results.py", title="View results"),
    ]
)
pg.run()
