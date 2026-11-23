st.space()
st.subheader("Scenario summary")
st.write(f"""
Summary of nurse queue times across **all** replications.

* Mean: {trial.trial_mean_q_time_nurse:.2f} minutes.
* SD: {trial.trial_sd_q_time_nurse:.2f} minutes.
* 90th Perc: {trial.trial_perc_90_q_time_nurse:.2f} minutes.
* Standard error: {trial.se_q_time_nurse:.2f}
* 95% CI: ({trial.ci_lower_q_time_nurse:.2f},
{trial.ci_upper_q_time_nurse:.2f}) minutes.

Total nurse staffing cost: £{trial.total_nurse_cost:,.2f}
""")

st.space()
st.subheader("Results from individual replications")
st.write(
    "The chart shows how the mean nurse queue time varies between **individual** replications."
)

fig = px.histogram(
    data_frame=trial.replication_df,
    x="mean_q_time_nurse",
)
fig.update_layout(
    xaxis_title="Mean nurse queue time",
    yaxis_title="Number of replications"
)
st.plotly_chart(fig)

with st.expander("View underlying data from each replication"):

    underlying = trial.replication_df[
            [
                "replication_id",
                "patient_counter",
                "mean_q_time_nurse",
                "sd_q_time_nurse",
                "perc_90_q_time_nurse",
            ]
        ]

    st.dataframe(underlying)

    st.download_button(
        label="Download table as CSV",
        data=underlying.to_csv().encode("utf-8"),
    )