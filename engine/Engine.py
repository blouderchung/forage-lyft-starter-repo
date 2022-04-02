from abc import ABC

class Engine(ABC):
    def __init__(self, last_service_date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
    
    def needs_service(self):
        pass