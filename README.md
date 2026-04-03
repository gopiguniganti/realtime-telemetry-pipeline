# Realtime Telemetry Pipeline

A personal data engineering project that demonstrates how to ingest, process, and visualize live telemetry data using a simple local stack.

## Why this project exists

This repository is meant to showcase practical data engineering habits for building a small but realistic telemetry pipeline:

- collecting data from a source
- sending it to a time-series store
- visualizing it through dashboards
- packaging the setup with Docker for easy local runs

## Tech stack

- Python for the ingestion worker
- InfluxDB for time-series storage
- Grafana for visualization
- Docker Compose for local orchestration

## Repository structure

```text
telemetry-pipeline/
├── docker/                  # Docker Compose and runtime configuration
├── docs/                    # architecture notes and dashboard assets
├── scripts/                 # ingestion and helper scripts
├── requirements.txt         # Python dependencies
└── README.md
```

## Local setup

```bash
git clone https://github.com/gopiguniganti/realtime-telemetry-pipeline.git
cd realtime-telemetry-pipeline
docker compose -f docker/docker-compose.yml up -d
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./scripts/run.sh
```

## What’s included

- a starter Docker stack for InfluxDB and Grafana
- a Python ingestion example that writes points to InfluxDB
- a dashboard template file for future Grafana work
- a run script to simplify local execution

## Roadmap

- [x] initial project scaffold
- [x] add ingestion script
- [x] add dashboard template
- [ ] connect Grafana with a real dashboard
- [ ] add sample data model and documentation
- [ ] add CI checks and deployment notes
