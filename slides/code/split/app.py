"""Entrypoint for app. Defines navigation."""

import streamlit as st

pg = st.navigation(
    [
        st.Page("home.py", title="Home"),
        st.Page("simulation.py", title="Run simulation"),
    ]
)

pg.run()

# Session state set-up
# Doing it here as otherwise if click straight on view results get error
if "scenarios" not in st.session_state:
    st.session_state.scenarios = {}
