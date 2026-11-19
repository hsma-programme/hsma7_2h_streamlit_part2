if not st.session_state.scenarios:
    st.info("Run and save scenarios to view results here.", icon="ℹ️")

else:
    st.space()
    with st.container(border=True):
        st.selectbox(
            label="**Choose a scenario to view:**",
            options=list(st.session_state.scenarios),
            key="chosen_scenario",
        )
    
    ...