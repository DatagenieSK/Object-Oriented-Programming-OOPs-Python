# Static methods = A method that belong to a class rather than any object from that class (instance)
#usually used for general utility functions

#instance methods = Best for operations on instance of the class (object)
#static = BEst for utility functions that do need access to class data

class Emplyee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"


    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager", "developer", "annalytic"]
        return position in valid_position



print(Emplyee.is_valid_position("manager"))
print(Emplyee.is_valid_position("Rocket Scientist")) #no need to craete instace to access the static method

employee1 = Emplyee("Md shazad", "manager")

employee2 = Emplyee("Muddassar", "HR")


print(employee1.get_info())