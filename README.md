# Realtime Telemetry Pipeline

A personal data engineering project that demonstrates how to ingest, process, and visualize telemetry data using a Dockerized local stack. The repository is designed to look like a realistic, portfolio-ready example of a small but practical data pipeline.

## Why this project exists

This project showcases common data engineering patterns such as:

- collecting data from a source
- sending it into a time-series store
- visualizing it through dashboards
- packaging the workflow for local repeatability
- extending the design toward vehicle telemetry with an OBD2 workflow

## Tech stack

- Python for the ingestion workers
- InfluxDB for time-series storage
- Grafana for visualization
- Docker Compose for local orchestration

## Repository structure

```text
telemetry-pipeline/
├── docker/                  # Docker Compose and runtime configuration
├── docs/                    # architecture notes, workflow docs, and setup guides
├── scripts/                 # ingestion and helper scripts
├── requirements.txt         # Python dependencies
├── Makefile                 # local setup and run shortcuts
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
- a placeholder OBD2 collector script for vehicle telemetry experiments
- a lightweight system metrics collector for host-level telemetry
- a dashboard template file for future Grafana work
- a Makefile for setup and run steps
- workflow notes for local demo usage

## OBD2 workflow

This repository also includes a simple OBD2-oriented path for future real-world vehicle telemetry integration:

- connect an ELM327-compatible adapter to the vehicle
- confirm data access with a mobile OBD app
- replace the placeholder generator with real PID reads
- publish those readings into InfluxDB
- visualize them in Grafana

## Architecture

A simple end-to-end flow for the system is documented in [docs/architecture-diagram.md](docs/architecture-diagram.md).

## Additional feature

A lightweight host metric collector is documented in [docs/system-metrics.md](docs/system-metrics.md).

## Roadmap

- [x] initial project scaffold
- [x] add ingestion script
- [x] add dashboard template
- [x] add demo workflow and local automation
- [x] add OBD2 integration scaffold
- [ ] connect Grafana with a real dashboard
- [ ] add CI checks and deployment notes
