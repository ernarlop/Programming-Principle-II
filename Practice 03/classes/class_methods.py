#Methods with Parameters
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(7, 6))
print(calc.multiply(4, 3))

# Second Example
class Person:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city

  def get_info(self):
    return f"{self.name} is {self.age} years old and from {self.city}"

p1 = Person("Yernar", 20, "Atyrau")
print(p1.get_info())


# Third Example
class Person:
  def __init__(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city
  def __str__(self):
    return f"{self.name} ({self.age}) from {self.city}"

p1 = Person("Yernar", 20, "Atyrau")
print(p1)


# Fourth Example
class Cinema_Film:
  def __init__(self, film):
    self.film = film
    self.films = []

  def add_film(self, film):
    self.films.append(film)
    print(f"Added: {film}")

  def remove_film(self, film):
    if film in self.films:
      self.films.remove(film)
      print(f"Removed: {film}")

  def show_films(self):
    print(f"Cinemas for today '{self.film}':")
    for film in self.films:
      print(f"- {film}")

my_playlist = Cinema_Film("Favorites")
my_playlist.add_film("Dastur")
my_playlist.add_film("Gashykpyn sagan")
my_playlist.show_films()