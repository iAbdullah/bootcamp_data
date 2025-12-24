import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd
from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv, write_parquet

def main():
    p = make_paths(ROOT)
    df = read_orders_csv(p.raw / "orders.csv")
    write_parquet(df, p.processed / "orders.parquet")
    print(f"Loaded {len(df)} rows to orders.parquet")

if __name__ == "__main__":
    main()