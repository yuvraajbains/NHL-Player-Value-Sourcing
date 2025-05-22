# src/generate_graphs.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from preprocess import load_sample_data
from value_model import calculate_value_score

def generate_value_bar_chart():
    df = load_sample_data()
    df = calculate_value_score(df)

    df = df.sort_values("ValueScore", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(df["Name"], df["ValueScore"], color='skyblue')
    plt.xlabel("Value Score")
    plt.title("Player Value Score Ranking")
    plt.gca().invert_yaxis()

    os.makedirs("outputs/graphs", exist_ok=True)
    output_path = "outputs/graphs/value_score_bar_chart.png"
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"✅ Chart saved to {output_path}")

if __name__ == "__main__":
    generate_value_bar_chart()
