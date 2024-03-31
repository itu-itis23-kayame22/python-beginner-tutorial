# Objects

age = 8

print(age.real)
print(age.imag)

# Loops
# continue skip the iteration
# break breaks the block


# Classes
class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

roger.walk()

# Modules
# import defined file

import math

print(math.sqrt(4))

