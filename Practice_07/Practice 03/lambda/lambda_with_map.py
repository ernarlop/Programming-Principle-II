# This code demonstrates the use of lambda functions with the map() function to perform operations on lists.
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Second example
Phones = ["iPhone", "Samsung", "OnePlus", "Google Pixel"]
version_PRO = list(map(lambda x: x + " Pro", Phones))
print(version_PRO)


# Third example
recent_years = [2020, 2021, 2022, 2023]
next_years = list(map(lambda x: x + 1, recent_years))
print(next_years)


# Fourth example
names = ["Alice", "Bob", "Charlie", "David"]
greeting = list(map(lambda x: "Hello, " + x + "!", names))
print(greeting)

