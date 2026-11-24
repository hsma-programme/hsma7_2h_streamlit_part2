import streamlit as st

grid = st.grid()

grid.metric(
    label="Average daily referrals",
    value=120,
    delta="10 vs last year",
    delta_color="red"
)

grid.metric(
    label="Staffed beds",
    value=32,
    delta="4 vs last year",
    delta_color="green",
)