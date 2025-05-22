import pandas as pd

def calculate_value_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Clean PlusMinus if it's like "+35"
    df["PlusMinus"] = df["PlusMinus"].astype(str).str.replace("+", "", regex=False).astype(float)

    # Prevent divide-by-zero
    df["CapHit"] = df["CapHit"].replace(0, 1e-6)
    df["TOI"] = pd.to_numeric(df["TOI"], errors="coerce").replace(0, 1e-6)

    # Derived stats
    df["Points"] = df["Goals"] + df["Assists"]
    df["GoalsPerMillion"] = df["Goals"] / df["CapHit"]
    df["EfficiencyIndex"] = df["Points"] / df["TOI"]

    # NEW: Normalize each stat (min-max scale between 0–1)
    df["Norm_GoalsPerMillion"] = (df["GoalsPerMillion"] - df["GoalsPerMillion"].min()) / (df["GoalsPerMillion"].max() - df["GoalsPerMillion"].min())
    df["Norm_EfficiencyIndex"] = (df["EfficiencyIndex"] - df["EfficiencyIndex"].min()) / (df["EfficiencyIndex"].max() - df["EfficiencyIndex"].min())
    df["Norm_PlusMinus"] = (df["PlusMinus"] - df["PlusMinus"].min()) / (df["PlusMinus"].max() - df["PlusMinus"].min())

    # Weighted final score
    df["ValueScore"] = (
        0.4 * df["Norm_GoalsPerMillion"] +
        0.4 * df["Norm_EfficiencyIndex"] +
        0.2 * df["Norm_PlusMinus"]
    )

    return df.sort_values("ValueScore", ascending=False)
