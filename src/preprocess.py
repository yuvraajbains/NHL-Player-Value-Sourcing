import pandas as pd

def load_sample_data(filepath: str = "data/nhl_sample_players.csv") -> pd.DataFrame:
    """
    Loads NHL sample skater data from a CSV file.
    
    Returns:
        DataFrame: Cleaned player data
    """
    df = pd.read_csv(filepath)

    # Normalize TOI column to float (in minutes)
    df["TOI"] = df["TOI"].astype(float)

    # Normalize CapHit column to float (strip $ if needed)
    df["CapHit"] = df["CapHit"].astype(str).str.replace("$", "").astype(float)

    return df
