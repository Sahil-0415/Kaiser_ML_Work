# 1. Define the class
class Dog:
    # The constructor method initializes the object's attributes
    def __init__(self, name, breed):
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute

    # A simple method (action)
    def bark(self):
        return f"{self.name} says Woof!"

# 2. Create objects (instances) of the class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# 3. Access attributes and call methods
print(f"Dog 1 is a {dog1.breed} named {dog1.name}.")
print(dog1.bark())

print(f"Dog 2 is a {dog2.breed} named {dog2.name}.")
print(dog2.bark())
