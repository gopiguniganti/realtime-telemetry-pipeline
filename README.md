# Realtime Telemetry Pipeline

I built this project to explore telemetry ingestion, storage, and visualization with a small local stack. It brings together Python, InfluxDB, Grafana, and Docker to create a simple workflow for collecting and reviewing time-series data.

## What I built

The project covers a few practical pieces of the workflow:

- collecting sample telemetry data from a Python script
- sending data into InfluxDB for time-series storage
- visualizing the data in Grafana
- keeping the stack repeatable with Docker Compose and a small Makefile
- leaving room for future work with vehicle telemetry and more realistic collectors

## Tools and skills used

- Python for the ingestion logic
- Docker Compose for local service orchestration
- InfluxDB for time-series storage
- Grafana for dashboards and visualization
- Git for version control and project organization

## Repository structure

```text
telemetry-pipeline/
├── docker/                  # Docker Compose and runtime configuration
├── docs/                    # architecture notes and workflow documentation
├── scripts/                 # ingestion and helper scripts
├── tests/                   # regression tests for the collector logic
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
make test
```

## Current capabilities

- a local InfluxDB and Grafana stack
- a Python telemetry writer that sends tagged measurements to InfluxDB
- a simple regression test for the payload builder
- a small Makefile workflow for setup and testing

## Architecture

A high-level overview of the flow is documented in [docs/architecture-diagram.md](docs/architecture-diagram.md).

## Next steps

- add more realistic system metrics collection
- expand the dashboard views in Grafana
- add alerts and operational monitoring
- connect additional data sources such as OBD2 telemetry
