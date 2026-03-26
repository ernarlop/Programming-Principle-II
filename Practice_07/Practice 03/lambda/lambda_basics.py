# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(3))

x = lambda a : a + 3
print(x(10))

x = lambda a : a + 5
print(x(8))

x = lambda a : a + 12
print(x(1))


# We can use one lambda for multiple variables
x = lambda a, b : a + b
print(x(7, 6))

x = lambda a, b : a + b
print(x(9, 4))

x = lambda a, b, c : a + b + c
print(x(3, 4, 6))

x = lambda a, b, c, d : a + b + c + d
print(x(2, 3, 4, 4))

# We could use lambda functions inside another function
def Yernar(n):
  return lambda a : a * n   

DateOfBirth = Yernar(1)

print(DateOfBirth(13))



def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(3)

print(mydoubler(2))



def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(7)

print(mydoubler(5))