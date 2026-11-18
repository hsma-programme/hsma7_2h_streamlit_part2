    # Save results to session state to allow comparison between scenarios
    scenario_name = f"Scenario {len(st.session_state.scenarios) + 1}"
    st.session_state.scenarios[scenario_name] = {
        "settings": {
            "Scenario": scenario_name,
            "Inter-arrival": st.session_state.mean_patient_inter,
            "Consultation mean": st.session_state.mean_nurse_consult_time,
            "Consultation SD": st.session_state.sd_nurse_consult_time,
            "Nurses": st.session_state.num_nurses,
            "Cost per hour": st.session_state.nurse_cost_per_hour,
            "Duration": st.session_state.sim_duration,
            "Replications": st.session_state.num_replications,
        },
        "mean": trial.trial_mean_q_time_nurse,
        "sd": trial.trial_sd_q_time_nurse,
        "p90": trial.trial_perc_90_q_time_nurse,
        "se": trial.se_q_time_nurse,
        "ci_lower": trial.ci_lower_q_time_nurse,
        "ci_upper": trial.ci_upper_q_time_nurse,
        "cost": trial.total_nurse_cost,
        "df": trial.replication_df,
    }
