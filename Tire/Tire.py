from abc import ABC

class Tire(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    def needs_service(self):
        pass