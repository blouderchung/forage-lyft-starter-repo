from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        totalDays = self.current_date - self.last_service_date
        if totalDays >= 365 * 4:
            return True
        return False
