from Battery import NubbinBattery, SpindlerBattery
from Engine import capulet_engine, sternman_engine, willoughby_engine
from Tire import Tire
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(current_date,last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        tire = Tire()

        car = Car(battery, engine, tire)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Tire()
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = sternman_engine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Tire()
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Tire()
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Tire()
        car = Car(engine, battery, tire)
        return car