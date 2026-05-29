"""
Base Sensor class for the Orion 7 telemetry library.

Anika drafted this when she started extending the library to handle
different sensor types. It works for the simple cases but I'm not sure
it's the right shape long-term. Worth a look before we add any more
sensor types. - Felix
"""

from datetime import datetime, timezone


class Sensor:
    """Base class for all telemetry sensors."""

    def __init__(self, sensor_id, unit):
        self.sensor_id = sensor_id
        self.unit = unit
        self.status = "nominal"
        self._last_value = None
        self._last_timestamp = None

    def read(self, value):
        """Record a new reading from the sensor."""
        self._last_value = value
        self._last_timestamp = datetime.now(timezone.utc).isoformat()
        return self._last_value

    def validate(self):
        """Check the most recent reading is within acceptable bounds.

        Subclasses should override this to add type-specific validation.
        The base implementation just checks a value has been recorded.
        """
        if self._last_value is None:
            return False
        return True

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

    def mark_degraded(self):
        self.status = "degraded"

    def mark_nominal(self):
        self.status = "nominal"
