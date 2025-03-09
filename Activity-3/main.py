class Parrot:
 # class attribute
 species = "bird"

 # instance attribute
 def __init__(self, name, age):
  self.name = name
  self.age = age 

# instance the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attribute
print("Blu is a {}". format(blu.species))
print("woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} year old".format(blu.name, blu.age))
print("{} is {} year old".format(woo.name, woo.age))