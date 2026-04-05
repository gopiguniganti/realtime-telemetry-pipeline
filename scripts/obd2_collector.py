#!/usr/bin/env python3
import os
import random
import time
import requests

INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "my-super-secret-token")
ORG = os.getenv("INFLUX_ORG", "myorg")
BUCKET = os.getenv("INFLUX_BUCKET", "telemetry")


def write_point(measurement: str, field: str, value: float) -> None:
    payload = f"{measurement},{field}={value}"
    url = f"{INFLUX_URL}/api/v2/write?org={ORG}&bucket={BUCKET}&precision=s"
    headers = {"Authorization": f"Token {INFLUX_TOKEN}"}
    response = requests.post(url, headers=headers, data=payload, timeout=10)
    response.raise_for_status()


if __name__ == "__main__":
    while True:
        write_point("vehicle_metrics", "rpm", random.randint(800, 3000))
        write_point("vehicle_metrics", "speed", random.randint(0, 120))
        write_point("vehicle_metrics", "coolant_temp", random.randint(80, 110))
        time.sleep(10)
