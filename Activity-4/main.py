class Parrot:

    # intance attributes
    def_init_(self, name, age):
    self.name = name 
    self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
    # instantiate the object
    blu = Parrot("Blu",10)

    # call our instance mathods
    print(blu.sing("'Happy'"))
    print(blu.dance())