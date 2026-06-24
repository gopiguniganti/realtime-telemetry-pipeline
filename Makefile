PYTHON ?= python3
VENV ?= .venv

.PHONY: setup run stop test

setup:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r requirements.txt

run:
	. $(VENV)/bin/activate && $(PYTHON) scripts/send_to_influx.py

test:
	. $(VENV)/bin/activate && $(PYTHON) -m pytest -q

stop:
	docker compose -f docker/docker-compose.yml down
