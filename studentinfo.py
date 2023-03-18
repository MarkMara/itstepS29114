class Student:
    def __init__(self):
        self.height = 170
        self.age = 14
        self.name = "Mark"

    def GetFullInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nHeight: {self.height}"
