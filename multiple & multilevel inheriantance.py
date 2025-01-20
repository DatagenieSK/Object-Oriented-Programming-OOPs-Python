#multiple inheriantance = inherit from more than  one parent class


#multilevel = inherit from a parent which inherits from another parent

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} animal is eating")

    def sleep(self):
        print(f"{self.name} animal is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} animal Flee")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} animal hunt")

class Rabbit(Prey):

    def run(self):
        print(f"{self.name} can run")

class Fish(Prey,Predator):
    def swim(self):
        print(f"{self.name} can swim")



class Hawk(Predator):
    def fly(self):
        print(f"{self.name} can fly")


rabbit = Rabbit("bunny")
hank = Hawk("tony")
fish = Fish("nemo")


rabbit.flee()
hank.hunt()
fish.hunt()
fish.flee()
rabbit.run()
fish.swim()
fish.eat()
hank.eat()
rabbit.sleep()
rabbit.run()