from pathlib import Path
import pandas as pd

# Define standard missing value markers
NA = ["", "NA", "N/A", "null", "None"]

def read_orders_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        # Keep IDs as strings to preserve leading zeros
        dtype={"order_id": "string", "user_id": "string"},
        na_values=NA,
        keep_default_na=True,
    )

def read_users_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype={"user_id": "string"},
        na_values=NA,
        keep_default_na=True,
    )

def write_parquet(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Save as Parquet to preserve data types
    df.to_parquet(path, index=False)