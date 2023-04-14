class Parent1:
    def __init__(self):
        self.attribute1 = "attribute1"

    def method1(self):
        print("method1 from Parent1")


class Parent2:
    def __init__(self):
        self.attribute2 = "attribute2"

    def method2(self):
        print("method2 from Parent2")


class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.attribute3 = "attribute3"

    def method3(self):
        print("method3 from Child")

obj = Child()
print(obj.attribute1)
print(obj.attribute2)
print(obj.attribute3)
obj.method1()
obj.method2()
obj.method3()
