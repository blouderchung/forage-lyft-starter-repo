from abc import ABC

class Battery(ABC):
    def __init__(self) -> None:
        super()

    def needs_service(self):
        pass