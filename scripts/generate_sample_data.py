"""
generate_sample_data.py

Generates a realistic, illustrative daily load-shedding dataset for South Africa
covering Jan 2022 - Dec 2025.

WHY SAMPLE DATA:
Real historical stage-by-stage data is available live from the EskomSePush API
(https://esp.info/) once you register for a free API key. This script exists so
you can build and test the entire pipeline (database, SQL, analysis, dashboard)
right now, without waiting on an API key or internet access.

The patterns below are modelled on publicly reported trends (e.g. worse winters,
the severe 2022-2023 period, gradual improvement through 2024-2025) but the exact
daily values are SYNTHETIC. Before using this project for real analysis or in an
interview, swap this file's output for real data using fetch_live_data.py.

Output: data/eskom_stages.csv
Columns:
    date            (YYYY-MM-DD)
    stage           (0-8, national load-shedding stage for that day - daily max)
    hours_shed      (estimated hours without power that day, derived from stage)
    season          (winter / summer, for seasonal analysis)
"""

import csv
import random
from datetime import date, timedelta

random.seed(42)  # reproducible output

START = date(2022, 1, 1)
END = date(2025, 12, 31)

# Roughly: higher stage = more hours shed per day. This mapping is a simplified,
# commonly used estimate (each stage ~= 2 extra hours of shedding per day).
HOURS_PER_STAGE = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16}


def season_of(d: date) -> str:
    # Southern Hemisphere: winter = May-Aug
    return "winter" if d.month in (5, 6, 7, 8) else "summer"


def base_stage_for_period(d: date) -> float:
    """Rough national severity trend by year, used as a midpoint for randomness."""
    if d.year == 2022:
        base = 3.5
    elif d.year == 2023:
        base = 4.5   # worst year on record nationally
    elif d.year == 2024:
        base = 1.5   # marked improvement from Sept 2023 onward
    else:  # 2025
        base = 0.8   # further stabilisation
    if season_of(d) == "winter":
        base += 1.2  # winter demand pushes stages up
    return base


def sample_stage(d: date) -> int:
    base = base_stage_for_period(d)
    noise = random.gauss(0, 1.3)
    stage = round(base + noise)
    return max(0, min(8, stage))


def main():
    rows = []
    d = START
    while d <= END:
        stage = sample_stage(d)
        rows.append({
            "date": d.isoformat(),
            "stage": stage,
            "hours_shed": HOURS_PER_STAGE[stage],
            "season": season_of(d),
        })
        d += timedelta(days=1)

    out_path = "data/eskom_stages.csv"
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "stage", "hours_shed", "season"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    main()
