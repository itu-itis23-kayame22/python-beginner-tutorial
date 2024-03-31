#STRINGS

name = "Beau"
name += "is my name"
age = str(39)
print(name)

print(""" Beau is
      39
      years old
      """)


#methods
string = "fatih kaya"
string.upper() #FATIH KAYA #or use isupper to check
string.lower()
string.title() #Fatih Kaya

print("at" in string)

#for escape / use backslash

#NUMBERS
num = complex(2,3)#for complex numbers
print(round(5.1))

#Enum
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)