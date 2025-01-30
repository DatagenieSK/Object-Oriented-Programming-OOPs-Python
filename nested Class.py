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
        def  __init__(self,name,position):
            self.name = name
            self.positions = position

        def get_details(self):
            return f"{self.name} {self.positions}"

    def __init__(self,company_name):
        self.company_name = company_name
        self.employee = []

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employee.append(new_employee)

    def list_employee(self):
        return [employee.get_details() for employee in self.employee]





company = Company("TCS")

company_1 = Company("OLA")

company.add_employee('Sk', 'manager')
company.add_employee("anna", 'manager')

company_1.add_employee("md", "agent")
company_1.add_employee("muddassar", "HR")

print(company.company_name)

#print(company.list_employee())

for employee in company.list_employee():
    print(employee)
print(company_1.company_name)
for employee in company_1.list_employee():
    print(employee)