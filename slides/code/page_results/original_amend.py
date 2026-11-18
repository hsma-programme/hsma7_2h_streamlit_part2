import pandas as pd
import plotly.express as px
import streamlit as st

# Get results of chosen scenario
results = st.session_state.scenarios[st.session_state.chosen_scenario]

st.space()
st.subheader("Scenario summary")
st.write(f"""
Summary of nurse queue times across **all** replications.

* Mean: {results["mean"]:.2f} minutes.
* SD: {results["sd"]:.2f} minutes.
* 90th Perc: {results["p90"]:.2f} minutes.
* Standard error: {results["se"]:.2f}
* 95% CI: ({results["ci_lower"]:.2f}, {results["ci_upper"]:.2f}) minutes

Total nurse staffing cost: £{results["cost"]:,.2f}
""")

st.space()
st.subheader("Results from individual replications")
st.write(
    "The chart shows how the mean nurse queue time varies between **individual** replications."
)

fig = px.histogram(
    data_frame=results["df"],
    x="mean_q_time_nurse",
)
fig.update_layout(
    xaxis_title="Mean nurse queue time",
    yaxis_title="Number of replications"
)
st.plotly_chart(fig)

with st.expander("View underlying data from each replication"):
    st.dataframe(
        results["df"][
            [
                "replication_id",
                "patient_counter",
                "mean_q_time_nurse",
                "sd_q_time_nurse",
                "perc_90_q_time_nurse",
            ]
        ]
    )