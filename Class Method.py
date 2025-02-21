'''
Class method = allow operation related to the class itself
               take (cls) as the first parameter, which represent the class itself
'''

class Students:

    count = 0
    total_gpa = 0
    def __init__(self, name,gpa):
        self.name = name
        self.gpa = gpa
        Students.count +=1
        Students.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"


    @classmethod
    def get_count(cls):
        return f"tottal number of student {cls.count}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Avg GPA = {cls.total_gpa / cls.count}"


student1 = Students("Shazd", 6.5)
student2 = Students("alqamar", 7.85)
student3 = Students("adil", 8.5)

print(Students.get_count())

print(Students.get_avg_gpa())