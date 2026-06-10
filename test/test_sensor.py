from src.sensor import Sensor
from src.temperature_sensor import TemperatureSensor
from src.battery_sensor import BatterySensor
from src.heading_sensor import HeadingSensor
from src.distance_sensor import DistanceSensor
import pytest


def test_sensor_records_a_reading():
    sensor = TemperatureSensor(sensor_id="GENERIC_01")
    sensor.read(42.0)
    assert sensor._last_value == 42.0


def test_sensor_starts_nominal():
    sensor = HeadingSensor(sensor_id="GENERIC_01")
    assert sensor.status == "nominal"


def test_sensor_can_be_marked_degraded():
    sensor = BatterySensor(sensor_id="GENERIC_01")
    sensor.mark_degraded()
    assert sensor.status == "degraded"


def test_sensor_validate_fails_with_no_reading():
    sensor = TemperatureSensor(sensor_id="GENERIC_01")
    assert sensor.validate() is False


def test_sensor_validate_passes_with_a_reading():
    sensor = BatterySensor(sensor_id="GENERIC_01")
    sensor.read(42.0)
    assert sensor.validate() is True


def test_sensor_produces_a_packet():
    sensor = DistanceSensor(sensor_id="GENERIC_01")
    sensor.read(42.0)
    packet = sensor.to_packet(mission_elapsed_time=86401)
    assert packet["sensor_id"] == "GENERIC_01"
    assert packet["value"] == 42.0
    assert packet["unit"] == "metre"
    assert packet["mission_elapsed_time"] == 86401
    assert packet["status"] == "nominal"


def test_sensor_raises_type_error_when_using_sensor():
    with pytest.raises(TypeError):
        sensor = Sensor(sensor_id="GENERIC_01")

