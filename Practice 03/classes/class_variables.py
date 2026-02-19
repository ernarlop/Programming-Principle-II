# Class Variables in Python. Variables are containers for storing data values.
class Student:
    school_name = "AITU"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable
s1 = Student("Yernar")
s2 = Student("Azamat")

print(s1.school_name)
print(s1.name)


# Second Example
class Car:
    total_cars = 0   # class variable

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

c1 = Car("Toyota")
c2 = Car("BMW")
c3 = Car("Audi")

print(Car.total_cars)
print(c1.brand)


# Third Example
class Employee:
    company_name = "TechCorp"   # class variable

    def __init__(self, name, position):
        self.name = name
        self.position = position

e1 = Employee("Yernar", "Developer")
e2 = Employee("Azamat", "Manager")

print(e1.company_name)
print(e2.company_name)
print(e1.name)
print(e2.position)
print(e1.name + " will be a " + e2.position)


# Fourth Example
class grade : 
    student_name = "Yernar"  # class variable
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score
g1 = grade("Math", 80)
g2 = grade("Science", 80)
g3 = grade("PP2", 95)
AVG_GPA = (g1.score + g2.score + g3.score)/3
print(f"{g1.student_name}'s average GPA is {AVG_GPA}")
