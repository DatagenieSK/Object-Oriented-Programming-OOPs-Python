"""
nested class = a class defined within another class
class Outer:
    class Inner:

benefits : Allows you to logically group classes that are closely related
Encapsulates private detaild that aren't relevant outside of the outer class
keeps the namespace clean, reduces the possibility of naming conflits
"""


class Company:
    class Employee:
        pass

    def __init__(self,company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self, name, position):
        pass

    def list_employee(self):
        pass


company = Company("TCS")

print(company.company_name)