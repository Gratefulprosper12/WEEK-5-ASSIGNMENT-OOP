class Superman:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.__secret_identity = secret_identity  # Encapsulated attribute
        self.power_level = power_level

    @property
    def identity(self):
        return "Classified"  # Hides the secret identity

    def introduce(self):
        print(f"I am {self.name}! Power level: {self.power_level}")

    def use_power(self):
        print(f"{self.name} uses a generic superhero power!")

# Inheritance Example
class Ironhero(Superman):  # Tech-based superhero
    def __init__(self, name, secret_identity, power_level, armor_model):
        super().__init__(name, secret_identity, power_level)
        self.armor_model = armor_model  # New attribute
        self.__battery_level = 100  # Private attribute

    def use_power(self):  # Polymorphism - overrides parent method
        print(f"{self.name} activates {self.armor_model} armor! (Power: {self.power_level})")

    def recharge(self):
        self.__battery_level = 100
        print("Armor fully charged!")

# Usage
hero1 = Superman("Captain Python", "Alex Coder", 80)
hero2 = Ironhero("Iron Coder", "Tony Script", 95, "Mark-42")

hero1.introduce()
hero2.introduce()
hero1.use_power() 
hero2.use_power()  