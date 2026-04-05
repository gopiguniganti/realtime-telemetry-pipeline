# OBD2 setup

This project includes a placeholder OBD2 collector that is ready to be adapted to a real adapter.

## What you need
- an ELM327-compatible OBD2 adapter
- a vehicle with an OBD2 port
- a machine that can access the adapter over Bluetooth or USB

## Typical flow
1. Plug the adapter into the vehicle OBD2 port.
2. Pair the adapter to the machine over Bluetooth or connect it over USB.
3. Use a compatible OBD2 app to confirm communication.
4. Replace the placeholder data generation with real PID reads.
5. Publish the readings into InfluxDB for analysis in Grafana.

## Notes
- Some cheap adapters only support a subset of PIDs.
- The current collector is a scaffold for future real integration.
