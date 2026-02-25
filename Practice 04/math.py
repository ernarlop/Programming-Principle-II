import math
import random

# Built-in Math Functions

nums = [3, -7, 2, 10, -4]
print("nums:", nums)

print("min(nums):", min(nums))          # smallest value
print("max(nums):", max(nums))          # biggest value
print("abs(-7):", abs(-7))              # absolute value (distance from 0)

print("round(3.14159, 2):", round(3.14159, 2))  # rounding with decimals
print("round(2.5):", round(2.5))                # note: bankers rounding in Python

print("pow(2, 5):", pow(2, 5))          # 2^5
print("pow(2, 5, 7):", pow(2, 5, 7))    # (2^5) % 7 (modular exponent)
print()

# math Module Functions

x = 9
print("sqrt(9):", math.sqrt(x))         # square root

y = 4.2
print("ceil(4.2):", math.ceil(y))       # round up to next integer
print("floor(4.2):", math.floor(y))     # round down to previous integer

angle = math.pi / 2                     # 90 degrees in radians
print("sin(pi/2):", math.sin(angle))    # sine (expects radians)
print("cos(pi/2):", math.cos(angle))    # cosine (expects radians)

print("pi:", math.pi)                   # constant π
print("e:", math.e)                     # constant e
print()

# random Module


print("random():", random.random())     # float in [0.0, 1.0)

print("randint(1, 10):", random.randint(1, 10))  # integer from 1 to 10 (inclusive)

colors = ["red", "green", "blue", "yellow"]
print("choice(colors):", random.choice(colors))  # pick a random element

cards = ["A", "K", "Q", "J", "10"]
print("Before shuffle:", cards)
random.shuffle(cards)                   # shuffles list in-place
print("After shuffle:", cards)