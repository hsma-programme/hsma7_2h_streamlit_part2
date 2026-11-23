"""Simple single-page app."""

import streamlit as st
from model import Param, Trial

with st.container(border=True):
    st.subheader("Patients")

    st.slider(
        label="Mean patient inter-arrival time (minutes)",
        min_value=3.0,
        max_value=7.0,
        value=5.0,
        step=0.25,
        key="mean_patient_inter",
    )

    st.subheader("Nurses")

    mean_col, sd_col = st.columns(2)

    with mean_col:
        st.number_input(
            label="Mean consultation length (minutes)",
            min_value=3.0,
            max_value=9.0,
            value=6.0,
            key="mean_nurse_consult_time",
        )

    with sd_col:
        st.number_input(
            label="Standard deviation of consultation length (minutes)",
            min_value=0.0,
            value=1.0,
            key="sd_nurse_consult_time",
        )

    st.pills(label="Number of nurses", options=range(1, 5), default=1, key="num_nurses")

    st.number_input(
        label="Cost per nurse per hour (£)",
        min_value=0.0,
        value=30.0,
        step=1.0,
        key="nurse_cost_per_hour",
        help="Nurses are costed for the full simulation duration, including time when they are not seeing patients",
    )

    st.space(size="xxsmall")
    st.subheader("Simulation")

    st.slider(
        label="Simulation duration (minutes)",
        min_value=50,
        max_value=200,
        value=120,
        key="sim_duration",
    )

    st.slider(
        label="Number of replications",
        min_value=10,
        max_value=50,
        value=30,
        key="num_replications",
    )

if st.button("Run simulation", type="primary"):
    params = Param(
        mean_patient_inter=st.session_state.mean_patient_inter,
        mean_nurse_consult_time=st.session_state.mean_nurse_consult_time,
        sd_nurse_consult_time=st.session_state.sd_nurse_consult_time,
        num_nurses=st.session_state.num_nurses,
        sim_duration=st.session_state.sim_duration,
        num_replications=st.session_state.num_replications,
        nurse_cost_per_hour=st.session_state.nurse_cost_per_hour,
    )
    trial = Trial(param=params)
    trial.run_trial()
    trial.calculate_trial_results()
