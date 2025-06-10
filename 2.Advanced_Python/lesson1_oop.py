# OOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OOP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Making a template for a car blueprint
# You wanna make a template for cars (for each car) that can drive and stop
class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def drive(self):
        print(f"{self.name} is driving at {self.speed} km/h")
    
    def stop(self):
        print(f"{self.name} has stopped driving")

# now you can make cars from that blueprint
baleno = Car("Baleno Hatchback", 100)
civic = Car("Civic Turbo", 200)

# now make them drive and stop
baleno.drive()
civic.drive()
baleno.stop()
civic.stop()



# Making a blueprint for animals
class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def info(self):
        return (f"This {self.gender} {self.name} is a {self.age} months old")
    
    def speak(self):
        return (f"{self.name} speak!!")

# now create each animals
doggie = Animal("dog", 4, "female")
catty = Animal("cat", 12, "male")

# call them
doggie.info()
doggie.speak()
catty.info()

# or using loops
list_animals = [Animal("Dolphin", 23, "female"), Animal("Wolf", 31, "male")]
for i in list_animals:
    print(i.info())
    print(i.speak())


