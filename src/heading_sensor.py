"""Heading sensor. Used for orientation tracking on rovers and crewed vehicles."""

from src.sensor import Sensor


class HeadingSensor(Sensor):
    """Sensor for heading readings in degrees."""

    MIN_VALID = 0.0
    MAX_VALID = 360.0

    def __init__(self, sensor_id):
        super().__init__(sensor_id=sensor_id, unit="degree")

    def validate(self):
        if not super().validate():
            return False
        return self.MIN_VALID <= self._last_value <= self.MAX_VALID
