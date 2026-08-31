"""
fetch_live_data.py

OPTIONAL: pulls real, current load-shedding status from the EskomSePush API
(https://esp.info/) instead of the synthetic sample data.

Setup:
    1. Register for a free API key at https://esp.info/
    2. Set it as an environment variable before running:
         Windows (PowerShell):  $env:ESP_TOKEN="your-token-here"
         Mac/Linux:              export ESP_TOKEN="your-token-here"
    3. Run: python scripts/fetch_live_data.py

Note: the free tier only returns CURRENT status, not historical data, and has a
limited number of calls per day/month. This script fetches today's status and
appends it to data/eskom_stages_live.csv each time you run it - so if you run it
daily over a few weeks, you'll build up a small real dataset of your own.

For a full historical dataset, the synthetic data in generate_sample_data.py
(or a manually compiled dataset from public news reporting / EskomSePush's own
historical status page) is the practical option for a student project timeline.
"""

import csv
import os
from datetime import date, datetime
from pathlib import Path

import requests

API_URL = "https://developer.sepush.co.za/business/2.0/status"
OUT_PATH = Path("data/eskom_stages_live.csv")


def fetch_status(token: str) -> dict:
    headers = {"Token": token}
    response = requests.get(API_URL, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()


def append_row(stage: int):
    file_exists = OUT_PATH.exists()
    with open(OUT_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "fetched_at", "stage"])
        writer.writerow([date.today().isoformat(), datetime.now().isoformat(), stage])


def main():
    token = os.environ.get("ESP_TOKEN")
    if not token:
        raise SystemExit(
            "No API token found. Set the ESP_TOKEN environment variable first - "
            "see the instructions at the top of this file."
        )

    data = fetch_status(token)
    # Response shape includes a national stage under data["status"]["eskom"]["stage"]
    stage = int(data["status"]["eskom"]["stage"])
    append_row(stage)
    print(f"Recorded today's national stage: {stage} -> {OUT_PATH}")


if __name__ == "__main__":
    main()
