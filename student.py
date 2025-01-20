

class Student:
    year_of_passing = 2024 # this is class variable (this can be access from evertwhere #this is always outside the class conscuture
    num_student = 0 # this is also class variable
    def __init__(self, name, age):
        self.age = age
        self.name = name
        Student.num_student += 1 #here we are add 1 by increse in the number of student


student1 = Student("MD", 24)

student2 = Student("Rahul", 25)

student3 = Student("MUfti", 26)


print(student1.name)
print(student1.age)
print(student1.year_of_passing)
print(Student.num_student)
#best practice

print(Student.year_of_passing) #becaue it enhance readbility now by looking at this we can say this is class variable

print(f"My Graducating year is {Student.year_of_passing} and has {Student.num_student} student")