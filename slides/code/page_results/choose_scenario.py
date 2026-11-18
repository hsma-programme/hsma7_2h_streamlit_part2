with st.container(border=True):
    st.selectbox(
        label="**Choose a scenario to view:**",
        options=list(st.session_state.scenarios),
        key="chosen_scenario",
    )

    # Convert the settings dictionary into a dataframe
    settings = pd.DataFrame(
        [
            scenario["settings"]
            for scenario in st.session_state.scenarios.values()
        ]
    )

    # Show dataframe of saved scenarios, with chosen scenario highlighted
    st.caption("The selected scenario is highlighted below.")
    st.dataframe(
        style_settings(
            settings=settings,
            chosen_scenarios=[st.session_state.chosen_scenario],
        ),
        hide_index=True,
    )