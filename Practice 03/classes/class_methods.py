#Methods with Parameters
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(7, 6))
print(calc.multiply(4, 3))


class Person:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

  def get_info(self):
    return f"{self.name} is {self.age} years old and from {self.city}"

p1 = Person("Yernar", 20, "Atyrau")
print(p1.get_info())

class Person:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

  def get_info(self):
    return f"{self.name} is {self.age} years old and from {self.city}"

p1 = Person("Yernar", 20, "Atyrau")
print(p1)

