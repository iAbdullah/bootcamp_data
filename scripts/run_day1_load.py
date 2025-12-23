from pathlib import Path
import sys
import json
from datetime import datetime, timezone
import logging

# Make src/ folder importable
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

log = logging.getLogger(__name__)

from bootcamp_data.config import make_paths
from bootcamp_data.io import read_orders_csv, read_users_csv, write_parquet
from bootcamp_data.transforms import enforce_schema

def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    p = make_paths(ROOT)

    # Load and Transform
    orders = enforce_schema(read_orders_csv(p.raw / "orders.csv"))
    users = read_users_csv(p.raw / "users.csv")

    log.info("Loaded: orders=%s, users=%s", len(orders), len(users))

    # Save to processed folder as Parquet
    out_orders = p.processed / "orders.parquet"
    out_users = p.processed / "users.parquet"

    write_parquet(orders, out_orders)
    write_parquet(users, out_users)

    # Record metadata for the run
    meta = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "rows": {"orders": int(len(orders)), "users": int(len(users))},
    }
    (p.processed / "_run_meta.json").write_text(json.dumps(meta, indent=2))
    log.info("ETL Complete. Files written to: %s", p.processed)

if __name__ == "__main__":
    main()