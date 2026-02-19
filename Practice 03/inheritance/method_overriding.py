# Method Overriding in Python
class Bird:
    def move(self):
        print("Bird moves")
b = Bird()
b.move()  # Output: Bird moves

class Penguin(Bird):
    def move(self):
        print("Penguin swims")
p = Penguin()
p.move()  # Output: Penguin swims


# Second example of method overriding
class Person:
    def greet(self):
        print("Hello")

class Student(Person):
    def greet(self):
        print("Hi, I am a student of KBTU")
s = Student()
s.greet()  # Output: Hi, I am a student of KBTU


# Third example of method overriding
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is riding")
b = Bike()
b.move()  # Output: Bike is riding


# Fourth example of method overriding
class Animal:
    def sound(self):
        print("Some sound")

class Cow(Animal):
    def sound(self):
        print("Moo")
c = Cow()
c.sound() # Output: Moo

