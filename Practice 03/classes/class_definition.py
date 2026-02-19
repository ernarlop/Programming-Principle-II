# This code defines a class called MyClass with three class attributes: p1, p2, and p3.
# First create a class and add attributes to it. 
class MyClass:
    p1 = 2
    p2 = 4
    p3 = 6
    
#Then create three instances of the class and print the values of the attributes for each instance.
p1 = MyClass()
p2 = MyClass()
p3 = MyClass() 
print(p1.p1)
print(p2.p2)
print(p3.p3)

# Also you can delete an attribute from a class using the del statement.
del MyClass.p1

# Now if you try to access the deleted attribute, it will raise an AttributeError.

#class definitions cannot be empty, so we use the pass statement
class MyClass:
    pass