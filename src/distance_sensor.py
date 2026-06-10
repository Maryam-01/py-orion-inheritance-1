from src.sensor import Sensor



class DistanceSensor(Sensor):
    """Sensor for distance readings."""

    MIN_VALID = 0.0
    MAX_VALID = 1000.0

    def __init__(self, sensor_id):
        super().__init__(sensor_id=sensor_id, unit="metre")

    def validate(self):
        if not super().validate():
            return False
        return isinstance(self._last_value, (float, int)) and self.MIN_VALID <= self._last_value <= self.MAX_VALID


    def read(self, value):
        return super().read(value)

    
    def to_packet(self, mission_elapsed_time):
        """Produce a telemetry packet from the most recent reading."""
        return {
            "sensor_id": self.sensor_id,
            "timestamp": self._last_timestamp,
            "value": self._last_value,
            "unit": self.unit,
            "mission_elapsed_time": mission_elapsed_time,
            "status": self.status,
        }
