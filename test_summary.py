from src.genai_sumarizer import summarize_player_data
from src.preprocess import load_sample_data
from src.value_model import calculate_value_score

df = load_sample_data()
df_scored = calculate_value_score(df)

# Show top 3 value players
print("\n🏆 Top Players by Value Score:\n")
print(df_scored[["Name", "Team", "ValueScore"]].head(3))

# Generate summaries
for _, row in df_scored.iterrows():
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
    print(f"\n🔹 {row['Name']} Summary:\n{summary}")
