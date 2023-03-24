class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 0
        self.age = 1
        self.energy = 100
        self.happy = 100

    def __str__(self):
        return f"{self.name} ({self.species}): Hunger = {self.hunger}, Energy = {self.energy}, Happy = {self.happy}, Age = {self.age} year"

    def feed_the_cat(self):
        self.hunger -= 10
        self.energy += 5

    def play_with_cat(self):
        self.energy -= 10
        self.happy += 5

cat = Pet("Tommy", "cat")
print(cat)