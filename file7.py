# Docstrings

class Dog:
    """A class representing a dog"""
    def bark(self):
        """Let the dog bark"""

# Exceptions

class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('dog not found!')

# List Compression 
    
numbers = [1, 2, 3, 4, 5]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)

# Polymorphism

class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

# Operator overloading




        
