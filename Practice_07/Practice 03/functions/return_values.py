# Return values 

def my_function(x, y):
  return x + y
result = my_function(5, 5)
print(result)


def my_function(a, b, c, d):
  return a // b * c - d
result = my_function(5, 5, 5, 5)
print(result)


def list_of_phones():
  return ["iPhone", "Samsung", "Google Pixel"]
Phones = list_of_phones()
print(Phones[0])
print(Phones[1])
print(Phones[2])


def resolution():
  return (1980, 1080)
x, y = resolution()
print("Your screen resolution is", x, ":", y)


def names ( a = "Yernar", b = "Nurkozha", c = "Sultan", d = "Aigerim", e = "Diana"):
  return a
list_of_friends = names(a = "Yernar")
print(list_of_friends)


