#!/usr/bin/env python3
import os
import platform
import random
import time
from typing import Dict, Mapping

import requests

INFLUX_URL = os.getenv("INFLUX_URL", "http://localhost:8086")
INFLUX_TOKEN = os.getenv("INFLUX_TOKEN", "my-super-secret-token")
ORG = os.getenv("INFLUX_ORG", "myorg")
BUCKET = os.getenv("INFLUX_BUCKET", "telemetry")
HOSTNAME = os.getenv("HOSTNAME", platform.node())
SLEEP_SECONDS = int(os.getenv("SEND_INTERVAL_SECONDS", "5"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))


def build_line_protocol(measurement: str, fields: Mapping[str, float], tags: Mapping[str, str] | None = None) -> str:
    tag_string = ""
    if tags:
        tag_items = ",".join(f"{key}={value.replace(' ', '_')}" for key, value in sorted(tags.items()))
        tag_string = f",{tag_items}"

    field_items = ",".join(f"{key}={value}" for key, value in sorted(fields.items()))
    return f"{measurement}{tag_string} {field_items}"


def write_point(measurement: str, fields: Mapping[str, float], tags: Mapping[str, str] | None = None) -> None:
    payload = build_line_protocol(measurement=measurement, fields=fields, tags=tags)
    url = f"{INFLUX_URL}/api/v2/write?org={ORG}&bucket={BUCKET}&precision=s"
    headers = {"Authorization": f"Token {INFLUX_TOKEN}"}

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()
            return
        except requests.RequestException as exc:
            if attempt >= MAX_RETRIES:
                raise RuntimeError(f"Failed to write telemetry after {MAX_RETRIES} attempts: {exc}") from exc
            time.sleep(2 * attempt)


def collect_sample() -> tuple[str, Dict[str, float], Dict[str, str]]:
    metrics = {
        "cpu_percent": round(random.uniform(20, 90), 2),
        "memory_percent": round(random.uniform(40, 85), 2),
    }
    tags = {"host": HOSTNAME, "source": "demo"}
    return "system_metrics", metrics, tags


if __name__ == "__main__":
    while True:
        measurement, metrics, tags = collect_sample()
        write_point(measurement=measurement, fields=metrics, tags=tags)
        time.sleep(SLEEP_SECONDS)
