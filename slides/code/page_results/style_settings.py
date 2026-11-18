# Function for highlighting the row/s with the chosen scenario/s
def style_settings(settings, chosen_scenarios):
    def highlight(row):
        style = (
            "background-color: #dbeafe; color: #111827"
            if row["Scenario"] in chosen_scenarios
            else ""
        )
        return [style] * len(row)

    return settings.style.apply(highlight, axis=1).format(precision=2)