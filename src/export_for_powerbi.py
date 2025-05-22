# src/export_for_powerbi.py

import pandas as pd
from preprocess import load_sample_data
from value_model import calculate_value_score

def export_player_data():
    df = load_sample_data()
    df_scored = calculate_value_score(df)

    # Optional: Add Efficiency metrics
    df_scored["Points"] = df_scored["Goals"] + df_scored["Assists"]
    df_scored["GoalsPerMillion"] = df_scored["Goals"] / df_scored["CapHit"]
    df_scored["EfficiencyIndex"] = df_scored["ValueScore"] * 100

    # Export to CSV for Power BI
    df_scored.to_csv("data/export_nhl_players.csv", index=False)
    print("✅ Exported data/export_nhl_players.csv for Power BI!")

if __name__ == "__main__":
    export_player_data()
