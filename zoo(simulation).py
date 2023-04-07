class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def feed(self):
        print(f"{self.name} has been fed.")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to the zoo.")

    def feed_animals(self):
        print("Feeding animals in the zoo:")
        for animal in self.animals:
            animal.feed()