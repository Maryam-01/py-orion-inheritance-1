from src.distance_sensor import DistanceSensor





def test_exposes_sensor_id_correctly():
    sensor = DistanceSensor(sensor_id="100")
    assert sensor.sensor_id == "100"

def test_exposes_unit_correctly():
    sensor = DistanceSensor(sensor_id = "200")
    assert sensor.unit == "metre"


def test_reading_sensor_validates_in_range():
    sensor = DistanceSensor(sensor_id="TEMP_01")
    sensor.read(100)
    assert sensor.validate() is True

def test_reading_sensor_invalidates_string():
    sensor = DistanceSensor(sensor_id="TEMP_01")
    sensor.read("random")
    assert sensor.validate() is False



