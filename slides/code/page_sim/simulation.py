"""Simple single-page app."""

import streamlit as st
from model import Param, Trial


DEFAULTS = {
    "mean_patient_inter": 5.0,
    "mean_nurse_consult_time": 6.0,
    "sd_nurse_consult_time": 1.0,
    "num_nurses": 1,
    "nurse_cost_per_hour": 30.0,
    "sim_duration": 120,
    "num_replications": 30,
}


def reset_widgets():
    for key, value in DEFAULTS.items():
        st.session_state[key] = value


with st.container(border=True):
    st.subheader("Patients")

    st.slider(
        label="Mean patient inter-arrival time (minutes)",
        min_value=3.0,
        max_value=7.0,
        value=DEFAULTS["mean_patient_inter"],
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
            value=DEFAULTS["mean_nurse_consult_time"],
            key="mean_nurse_consult_time",
        )

    with sd_col:
        st.number_input(
            label="Standard deviation of consultation length (minutes)",
            min_value=0.0,
            value=DEFAULTS["sd_nurse_consult_time"],
            key="sd_nurse_consult_time",
        )

    st.pills(
        label="Number of nurses",
        options=range(1, 5),
        default=DEFAULTS["num_nurses"],
        key="num_nurses"
    )

    st.number_input(
        label="Cost per nurse per hour (£)",
        min_value=0.0,
        value=DEFAULTS["nurse_cost_per_hour"],
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
        value=DEFAULTS["sim_duration"],
        key="sim_duration",
    )

    st.slider(
        label="Number of replications",
        min_value=10,
        max_value=50,
        value=DEFAULTS["num_replications"],
        key="num_replications",
    )

with st.container(horizontal=True):
    run = st.button("Run and save scenario", type="primary")
    st.button("Reset to defaults", on_click=reset_widgets)

if run:
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
