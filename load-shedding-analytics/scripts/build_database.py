"""
build_database.py

Loads data/eskom_stages.csv into a local SQLite database (load_shedding.db),
applying the schema in sql/schema.sql and computing the estimated business
cost column.

Run this after generate_sample_data.py (or fetch_live_data.py).
"""

import csv
import sqlite3
from pathlib import Path

DB_PATH = Path("load_shedding.db")
SCHEMA_PATH = Path("sql/schema.sql")
CSV_PATH = Path("data/eskom_stages.csv")

# Illustrative assumption, documented in schema.sql and the README:
# estimated revenue lost per hour without power for a small/medium business.
COST_PER_HOUR_ZAR = 850


def main():
    if not CSV_PATH.exists():
        raise SystemExit(
            f"{CSV_PATH} not found. Run scripts/generate_sample_data.py first."
        )

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    with open(SCHEMA_PATH) as f:
        cur.executescript(f.read())

    with open(CSV_PATH) as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            year, month, _ = row["date"].split("-")
            stage = int(row["stage"])
            hours = float(row["hours_shed"])
            rows.append((
                row["date"],
                int(year),
                int(month),
                stage,
                hours,
                row["season"],
                round(hours * COST_PER_HOUR_ZAR, 2),
            ))

    cur.executemany(
        """
        INSERT INTO load_shedding_daily
            (date, year, month, stage, hours_shed, season, est_business_cost_zar)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )
    conn.commit()

    count = cur.execute("SELECT COUNT(*) FROM load_shedding_daily").fetchone()[0]
    print(f"Loaded {count} rows into {DB_PATH}")

    conn.close()


if __name__ == "__main__":
    main()
