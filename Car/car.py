from abc import ABC, abstractmethod
from Battery.Battery import Battery
from Engine.Engine import Engine
from Tire.Tire import Tire

class Car(ABC):
    def __init__(self, battery:Battery, engine:Engine, tire:Tire):
        super().__init__()
        self.battery = battery
        self.engine = engine
        self.tire = tire

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
