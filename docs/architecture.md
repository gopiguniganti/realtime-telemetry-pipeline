# Architecture

The project uses a lightweight local stack for telemetry ingestion and visualization:

- Python ingestion worker produces sample telemetry events.
- InfluxDB stores the time-series data.
- Grafana visualizes the data with dashboards.

This setup is intended to be simple to run locally with Docker.
