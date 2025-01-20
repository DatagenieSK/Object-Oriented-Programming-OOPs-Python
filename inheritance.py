#inheriance allows a class to inherit attributes for another class
#from parents to child



class Animals:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eating(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f'{self.name} is Sleeping')


class Dog(Animals):
    def speak(self):
        print("Woof!")


class Cat(Animals):
    def speak(self):
        print("Meow")


class Mouse(Animals):
    def speak(self):
        print("Squeek")


dog = Dog("Tommy")
cat = Cat("nikky")
mouse = Mouse("warmtail")


print(dog.name)
print(dog.is_alive)
dog.eating()
dog.sleep()

cat.eating()


cat.speak()