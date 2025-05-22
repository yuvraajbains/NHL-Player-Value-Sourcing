# src/save_summaries.py

import os
import re
from genai_sumarizer import summarize_player_data
from preprocess import load_sample_data
from value_model import calculate_value_score

def slugify(name):
    """Converts player name to a safe filename."""
    return re.sub(r'\W+', '_', name.strip().lower())

def export_summaries(output_dir="outputs/summaries"):
    os.makedirs(output_dir, exist_ok=True)

    df = load_sample_data()
    df = calculate_value_score(df)

    for _, row in df.iterrows():
        player_text = f"""
        Name: {row['Name']}
        Team: {row['Team']}
        Position: {row['Position']}
        Goals: {row['Goals']}
        Assists: {row['Assists']}
        Time on Ice per Game: {row['TOI']}
        Cap Hit: ${row['CapHit']}M
        Plus/Minus: {row['PlusMinus']}
        Value Score: {row['ValueScore']:.2f}
        """

        summary = summarize_player_data(player_text)
        filename = slugify(row['Name']) + ".md"
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {row['Name']} Summary\n\n")
            f.write(summary.strip())

    print(f"✅ Exported {len(df)} player summaries to '{output_dir}'")

if __name__ == "__main__":
    export_summaries()
