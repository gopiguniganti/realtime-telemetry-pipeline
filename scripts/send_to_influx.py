#!/usr/bin/env python3
import os
import sys
import time
import random
import requests

INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "admin")
ORG = os.getenv("INFLUX_ORG", "myorg")
BUCKET = os.getenv("INFLUX_BUCKET", "telemetry")


def write_point(value: float) -> None:
    payload = f"system_metrics value={value}"
    url = f"{INFLUX_URL}/api/v2/write?org={ORG}&bucket={BUCKET}&precision=s"
    headers = {"Authorization": f"Token {INFLUX_TOKEN}"}
    response = requests.post(url, headers=headers, data=payload, timeout=10)
    response.raise_for_status()


if __name__ == "__main__":
    while True:
        write_point(random.uniform(20, 90))
        time.sleep(5)
