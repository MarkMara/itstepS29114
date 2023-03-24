import Human as h

class Student(h.Human):

    def __init__(self, name, age, height, mark = 12, subject = "00P Python"):
        h.Human.__init__(name, age, height,)
        self.mark = mark
        self.subject = subject


    def showInfo(self):
        h.Human(showInfo.Human)
        print(f"Subject: {self.subject}\n"
              f"Mark: {self.mark}\n")

