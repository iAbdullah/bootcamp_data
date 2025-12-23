import pandas as pd

def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    """Standardizes data types and handles numeric errors."""
    return df.assign(
        order_id=df["order_id"].astype("string"),
        user_id=df["user_id"].astype("string"),
        # Use errors="coerce" to turn invalid text into NaN
        amount=pd.to_numeric(df["amount"], errors="coerce").astype("Float64"),
        quantity=pd.to_numeric(df["quantity"], errors="coerce").astype("Int64"),
    )