from abc import ABC, abstractmethod
#jo bhi classes inheriantace kr rahi h abstract class se usmai sare abstract method hone chaiye nh toh typeerror ayega
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass





class Car(Vehicle):
    def go(self):
        print("driving")

    def stop(self):
        print("Stopped")

class Bike:
    def go(self):
        print("Riding")
    def stop(self):
        print("bike stopped")

car = Car()

car.go()