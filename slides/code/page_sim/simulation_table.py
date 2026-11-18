if st.session_state.scenarios:
    st.divider()
    st.header("Saved scenarios")

    st.dataframe(
        [scenario["settings"] for scenario in st.session_state.scenarios.values()],
        hide_index=True,
    )
    st.caption("Scenarios are saved for the current session only.")