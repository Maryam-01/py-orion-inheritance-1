"""Battery sensor. Used for power system voltage monitoring."""

from src.sensor import Sensor


class BatterySensor(Sensor):
    """Sensor for battery voltage readings in volts."""

    MIN_VALID = 0.0
    MAX_VALID = 60.0

    def __init__(self, sensor_id):
        super().__init__(sensor_id=sensor_id, unit="volt")

    def validate(self):
        if not super().validate():
            return False
        return self.MIN_VALID <= self._last_value <= self.MAX_VALID
