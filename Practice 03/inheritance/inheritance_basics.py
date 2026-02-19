# Inheritance : basics of using it 
# First example
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")
        
d = Dog()
d.speak()
d = Cat()
d.speak()


# super() : allows us to call a method from the parent class
# Second example
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


# Third example 
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
r = Rectangle(5, 3)
print("Area of rectangle:", r.area())


# Fourth example
class shoes : 
    def __init__(self, brand):
        self.brand = brand

    def introduce(self):
        print("This is a", self.brand, "shoe")

class sports_shoes(shoes):
    def __init__(self, brand, sport):
        super().__init__(brand)
        self.sport = sport

    def introduce(self):
        super().introduce()
        print("It is designed for", self.sport)
s = sports_shoes("Nike", "Basketball")
s.introduce()
