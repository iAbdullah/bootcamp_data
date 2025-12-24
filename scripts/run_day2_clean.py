import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv, read_users_csv, write_parquet
from bootcamp_data.transforms import (
    enforce_schema, missingness_report, add_missing_flags, 
    normalize_text, apply_mapping
)
from bootcamp_data.quality import require_columns, assert_non_empty

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger(__name__)

def main() -> None:
    p = make_paths(ROOT)
    
    log.info("Loading raw inputs")
    orders_raw = read_orders_csv(p.raw / "orders.csv")
    users = read_users_csv(p.raw / "users.csv")
    
    require_columns(orders_raw, ["order_id", "user_id", "amount", "quantity", "created_at", "status"])
    assert_non_empty(orders_raw, "orders_raw")
    
    orders = enforce_schema(orders_raw)
    
    # Save missingness report
    rep = missingness_report(orders)
    reports_dir = ROOT / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    rep.to_csv(reports_dir / "missingness_orders.csv", index=True)
    
    log.info("Cleaning status column")
    status_norm = normalize_text(orders["status"])
    mapping = {"paid": "paid", "refund": "refund", "refunded": "refund"}
    status_clean = apply_mapping(status_norm, mapping)
    
    orders_clean = (
        orders.assign(status_clean=status_clean)
              .pipe(add_missing_flags, cols=["amount", "quantity"])
    )
    
    write_parquet(orders_clean, p.processed / "orders_clean.parquet")
    log.info("Wrote: data/processed/orders_clean.parquet")

if __name__ == "__main__":
    main()