st.title("View results")

if not st.session_state.scenarios:
    st.info("Run and save scenarios to view results here.", icon="ℹ️")

else:
    st.write(
        "You can either view results from a **single scenario**, or **compare across scenarios**."
    )

    tab_single, tab_compare = st.tabs(
        ["View single scenario", "Compare scenarios"]
    )

    with tab_single:
        st.space()
        with st.container(border=True):
            st.selectbox(
                label="**Choose a scenario to view:**",
                options=list(st.session_state.scenarios),
                key="chosen_scenario",
            )
            ...