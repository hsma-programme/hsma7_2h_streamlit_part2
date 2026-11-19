with tab_compare:
    if len(st.session_state.scenarios) < 2:
        st.info("Run at least two scenarios to enable comparison", icon="ℹ️")

    else:
        st.space()
        with st.container(border=True):
            chosen_compare = st.multiselect(
                label="**Choose scenarios to compare**",
                options=list(st.session_state.scenarios),
            )

            st.caption("The selected scenarios are highlighted below.")

            st.dataframe(
                style_settings(settings=settings, chosen_scenarios=chosen_compare),
                hide_index=True,
            )

        if len(chosen_compare) < 2:
            st.info("Choose at least two scenario to compare", icon="ℹ️")

        else:
            # Results - will write next