class Human:
    def __init__(self, role = 0, name = "Human Default value"):
        self.name = name
        self.role = role
    def showName(self):
        if(self.name != None or self.name != ""):
            print(f"Name: {self.name}")
        else:
            print("The attribute name is empty or none!")