from scripts import send_to_influx


def test_build_line_protocol_includes_tags_and_numeric_fields():
    payload = send_to_influx.build_line_protocol(
        measurement="system_metrics",
        fields={"cpu_percent": 41.2, "memory_percent": 63.7},
        tags={"host": "test-host", "source": "local"},
    )

    assert payload.startswith("system_metrics,host=test-host,source=local ")
    assert "cpu_percent=41.2" in payload
    assert "memory_percent=63.7" in payload
