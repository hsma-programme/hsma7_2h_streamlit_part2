st.subheader("Mean nurse queue time")
st.write(
    "Compare the mean nurse queue times across replications. "
    "Each point represents one replication."
)

# Combine replication results, adding a scenario label.
replications = pd.concat(
    [
        st.session_state.scenarios[name]["df"].assign(Scenario=name)
        for name in chosen_compare
    ],
    ignore_index=True,
)

fig = px.box(
    replications,
    x="Scenario",
    y="mean_q_time_nurse",
    color="Scenario",
    points="all",
    category_orders={"Scenario": [
        name for name in st.session_state.scenarios
        if name in chosen_compare
    ]},
    hover_data=["replication_id"],
)
fig.update_layout(
    yaxis_title="Mean nurse queue time",
    showlegend=False,
)
st.plotly_chart(fig)