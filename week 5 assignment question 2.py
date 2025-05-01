class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass  # Abstract method

class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🕊️")

class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐟")

class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")

# Polymorphism in action
animals = [
    Bird("Pigeon"),
    Fish("Salmon"),
    Snake("Viper")
]

for creature in animals:
    creature.move() 
