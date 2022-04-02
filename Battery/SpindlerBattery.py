import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date:datetime, current_date:datetime) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        totalDays = self.current_date - self.last_service_date
        if totalDays.days >= 365 * 3:
            return True
        return False
