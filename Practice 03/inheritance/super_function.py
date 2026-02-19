# First example of using super() in Python

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print("My grade is", self.grade)

s = Student("Yernar", 100)
s.introduce()


# Second example of using super() in Python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


c = Car("Toyota", "Corolla")
print(c.brand)
print(c.model)


# Third example of using super() in Python
class friends : 
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)
class best_friends(friends):
    def __init__(self, name, hobby):
        super().__init__(name)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print("My hobby is", self.hobby)
        
b = best_friends("Yernar", "Football")
b.introduce()


# Fourth example of using super() in Python
class university:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, my name is", self.name)
class student(university):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

    def introduce(self):
        super().introduce()
        print("My major is", self.major)
s = student("Yernar", "Computer Science")
s.introduce()
