#!/usr/bin/env python3
import os
import sys
import time
import random

# Placeholder ingestion script for the telemetry pipeline project.
# Replace this with your real collector logic later.

while True:
    payload = {
        "measurement": "system_metrics",
        "value": random.uniform(20, 90),
        "timestamp": int(time.time()),
    }
    print(payload)
    time.sleep(5)
