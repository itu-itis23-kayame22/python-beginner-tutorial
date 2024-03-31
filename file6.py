# Accepting Arguments
import sys

name = sys.argv[1]

print(sys.argv)

# lambda

multiply = lambda a, b : a * b
print(multiply(2, 4))

# map, filter, reduce
# map
numbers = [1, 2, 3]
result = map(lambda a : a * 2, numbers)
print(list(result))

# filter
numbers = [1, 2, 3]
result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))

 
# Recursion 

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(3))

# Decorators

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")
