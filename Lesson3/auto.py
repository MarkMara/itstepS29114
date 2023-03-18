import human as h

class Auto:

    def __init__(self, humans = [], brand = "Brand auto default"):
        self.humans = humans
        self.brand = brand
        self.passengers = []
        self.driver = []

    def addPassengers(self, human = h.Human()):
        self.passengers.append(human.name)

    def addDriver(self, human = h.Human()):
        self.driver.append(human.name)

    def showBrand(self):
        if (self.brand != None or self.brand != ""):
            print(f"Brand: {self.brand}")
        else:
            print("The attribute brand is empty or none!")