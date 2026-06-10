
class CalibratedSensor():
    """reading raw values, """

    def __init__(self, sensor, offset, scale):
        self.sensor = sensor
        self.offset = offset
        self.scale = scale
        
        
    
    def read(self, value):
        """"""
        calibrated = (value + self.offset) * self.scale
    
        return calibrated



 
    
