st.space()
st.subheader("Summary statistics")

summary = pd.DataFrame(
    [
        {
            "Scenario": name,
            "Mean": st.session_state.scenarios[name]["mean"],
            "SD": st.session_state.scenarios[name]["sd"],
            "90th percentile": st.session_state.scenarios[name]["p90"],
            "Standard error": st.session_state.scenarios[name]["se"],
            "95% CI lower": st.session_state.scenarios[name][
                "ci_lower"
            ],
            "95% CI upper": st.session_state.scenarios[name][
                "ci_upper"
            ],
        }
        for name in chosen_compare
    ]
)

st.caption("Nurse queue time summary statistics, in minutes:")

st.dataframe(
    summary.style.format(precision=2),
    hide_index=True,
)

costs = pd.DataFrame(
    [
        {
            "Scenario": name,
            "Total cost (£)": st.session_state.scenarios[name]["cost"],
        }
        for name in chosen_compare
    ]
)

st.caption("Total nurse staffing costs:")

st.dataframe(costs, hide_index=True)
