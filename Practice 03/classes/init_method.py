# Create a class
class Car :
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def description(self):
        return f"{self.year} {self.make} {self.model}"

my_car = Car("Toyota", "Corolla", 2020)

print(my_car.description())

# Without init method it will be like this
class Car:
    def description(self):
        return f"{self.year} {self.make} {self.model}"
my_car = Car()
my_car.make = "Toyota"
my_car.model = "Corolla"
my_car.year = 2020
print(my_car.description())


# Also you can create multiple instances of the class and assign different values to the attributes for each instance.
class time :
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def display_time(self):
        return f"{self.hour}:{self.minute}:{self.second}"
my_time = time(12, 30, 45)
print(my_time.display_time())



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"{self.name} is {self.age} years old."
p1 = Person("Yernar", 20)
p2 = Person("Aizhan", 19)
p3 = Person("Dastan", 21)

print(p1.display_info())
print(p2.name)
print(p3.age)