
    # Select the newly saved scenario and show confirmation
    st.session_state.chosen_scenario = scenario_name
    st.success(f"""
    {scenario_name} ran successfully and was saved for this sesssion.
    """)
