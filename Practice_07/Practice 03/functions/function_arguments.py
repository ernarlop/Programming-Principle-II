### Function Arguments
def first_example(name):
  print(name + " is learning Python!")

first_example("Yernar")
first_example("Nurkozha")
first_example("Sultan") 
# Yernar - Nurkozha - Sultan are arguments

### Mixing Positional and Keyword Arguments
def second_example(name, age):
    print(name + " is " + str(age) + " years old.")
second_example("Yernar", 19)
second_example("Nurkozha", 20)
second_example("Sultan", 21)

def third_example(name, age, city):
    print(name + " is " + str(age) + " years old and lives in " + city + ".")
third_example("Yernar", 19, "Almaty")
third_example("Nurkozha", 20, "Astana")
third_example("Sultan", 21, "Shymkent")


def last_example(animal, name, age):
  print("I have ", age, "year old", animal, "named", name)
last_example("cat", name = "Cherni", age = 2)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])
my_person = {"name": "Yernar", "age": 19}
my_function(my_person)