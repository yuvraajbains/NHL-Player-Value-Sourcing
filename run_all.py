

import os
import pandas as pd
from src.value_model import calculate_value_score
from src.preprocess import load_sample_data
from src.genai_sumarizer import summarize_player_data

df = load_sample_data()

df = calculate_value_score(df)

os.makedirs("data", exist_ok=True)
df.to_csv("data/export_nhl_players.csv", index=False)
print("✅ Exported: data/export_nhl_players.csv")

os.makedirs("outputs/summaries", exist_ok=True)

for _, row in df.iterrows():
    player_input = f"""
    Name: {row['Name']}
    Team: {row['Team']}
    Goals: {row['Goals']}
    Assists: {row['Assists']}
    Time on Ice per Game: {row['TOI']}
    Cap Hit: ${row['CapHit']}M
    Plus/Minus: {row['PlusMinus']}
    """
    summary = summarize_player_data(player_input)
    filename = row['Name'].lower().replace(" ", "_") + ".md"
    with open(f"outputs/summaries/{filename}", "w", encoding="utf-8") as f:
        f.write(f"# {row['Name']} Summary\n\n")
        f.write(summary.strip())

print("✅ Summaries generated to outputs/summaries/")
