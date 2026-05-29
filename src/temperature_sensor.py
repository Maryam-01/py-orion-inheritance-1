"""Temperature sensor. Used for hull and equipment temperature monitoring."""

from src.sensor import Sensor


class TemperatureSensor(Sensor):
    """Sensor for temperature readings in celsius."""

    MIN_VALID = -100.0
    MAX_VALID = 150.0

    def __init__(self, sensor_id):
        super().__init__(sensor_id=sensor_id, unit="celsius")

    def validate(self):
        if not super().validate():
            return False
        return self.MIN_VALID <= self._last_value <= self.MAX_VALID
