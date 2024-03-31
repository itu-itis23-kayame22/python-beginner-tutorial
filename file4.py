# Functions

def hello(name):
    if not name:
        return
    print('Hello' + ' ' + name + "!")

hello("Beau")

# variable scope
#global or local declarition decides usability of the variable

#nested functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    increment()

count()

