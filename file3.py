#LISTS
dogs = ["Roger", 1 , "Syd",True ,"Quincy", 7]
listb = []

dogs[2] = "Beau"
dogs.append("chiwava")
dogs.extend(listb) #merge 2 list
dogs.remove(1) 

print(dogs)

#items
items = ["Roger", 1 , "Syd",True ,"Quincy", 7]

items.insert(2, "test")
print(items)

itemscopy = items[:]
print(itemscopy)

#Tuples 
names = ("Roger", "Syd")

names[0]
names.index("Roger")

#DICTIONARIES
dog = {"name": "Roger", "age": 8, "color": "green"}

print(dog.get("name"))
print(dog.popitem())

print(dog.keys())

#Sets 
set1 = {"Roger", "Syd",}
set2 = {"Roger"}

intersect = set1 & set2
print(intersect)

