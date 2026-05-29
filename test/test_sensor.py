from src.sensor import Sensor


def test_sensor_records_a_reading():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    sensor.read(42.0)
    assert sensor._last_value == 42.0


def test_sensor_starts_nominal():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    assert sensor.status == "nominal"


def test_sensor_can_be_marked_degraded():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    sensor.mark_degraded()
    assert sensor.status == "degraded"


def test_sensor_validate_fails_with_no_reading():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    assert sensor.validate() is False


def test_sensor_validate_passes_with_a_reading():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    sensor.read(42.0)
    assert sensor.validate() is True


def test_sensor_produces_a_packet():
    sensor = Sensor(sensor_id="GENERIC_01", unit="generic")
    sensor.read(42.0)
    packet = sensor.to_packet(mission_elapsed_time=86401)
    assert packet["sensor_id"] == "GENERIC_01"
    assert packet["value"] == 42.0
    assert packet["unit"] == "generic"
    assert packet["mission_elapsed_time"] == 86401
    assert packet["status"] == "nominal"
