from src.temperature_sensor import TemperatureSensor
from src.heading_sensor import HeadingSensor
from src.battery_sensor import BatterySensor


def test_temperature_sensor_validates_in_range():
    sensor = TemperatureSensor(sensor_id="TEMP_01")
    sensor.read(-47.3)
    assert sensor.validate() is True


def test_temperature_sensor_rejects_out_of_range():
    sensor = TemperatureSensor(sensor_id="TEMP_01")
    sensor.read(500.0)
    assert sensor.validate() is False


def test_temperature_sensor_packet_uses_celsius():
    sensor = TemperatureSensor(sensor_id="TEMP_01")
    sensor.read(-47.3)
    packet = sensor.to_packet(mission_elapsed_time=100)
    assert packet["unit"] == "celsius"


def test_heading_sensor_validates_in_range():
    sensor = HeadingSensor(sensor_id="HDG_01")
    sensor.read(87.4)
    assert sensor.validate() is True


def test_heading_sensor_rejects_above_max():
    sensor = HeadingSensor(sensor_id="HDG_01")
    sensor.read(361.0)
    assert sensor.validate() is False


def test_heading_sensor_rejects_negative():
    sensor = HeadingSensor(sensor_id="HDG_01")
    sensor.read(-1.0)
    assert sensor.validate() is False


def test_heading_sensor_packet_uses_degree():
    sensor = HeadingSensor(sensor_id="HDG_01")
    sensor.read(87.4)
    packet = sensor.to_packet(mission_elapsed_time=100)
    assert packet["unit"] == "degree"


def test_battery_sensor_validates_in_range():
    sensor = BatterySensor(sensor_id="BAT_01")
    sensor.read(28.5)
    assert sensor.validate() is True


def test_battery_sensor_rejects_above_max():
    sensor = BatterySensor(sensor_id="BAT_01")
    sensor.read(100.0)
    assert sensor.validate() is False
