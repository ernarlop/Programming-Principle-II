# Iterators & Generators 

# Iterators: iter() and next()
nums = [10, 20, 30]
it = iter(nums)              # create an iterator from a list
print(next(it))              # 10
print(next(it))              # 20
print(next(it))              # 30

# Loop through an Iterator
words = ["hi", "hello", "bye"]
it2 = iter(words)            # iterator object
for w in it2:                # loop consumes the iterator
    print(w)

# Create an Iterator (custom class)

class CountUpTo:
    """
    Iterator that returns numbers from 1 to n.
    Implements __iter__() and __next__().
    """
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self           # an iterator must return itself

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUpTo(5)
for x in counter:
    print(x)

#  Generators: yield keyword

def simple_gen():
    yield "A"
    yield "B"
    yield "C"

g = simple_gen()
print(next(g))   # A
print(next(g))   # B
print(next(g))   # C

# Creating Generator Functions

def squares(n):
    """Yields squares from 1 to n."""
    for i in range(1, n + 1):
        yield i * i

for s in squares(6):
    print(s)


# Generator Expressions

gen_expr = (x * 2 for x in range(1, 6))   # like list comprehension, but lazy
for s in gen_expr:
    print(s)    