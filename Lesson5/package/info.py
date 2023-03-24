import os
global package_path
global package_name
if __package__ is None or __package__ == '':
    package_path = os.path.dirname(os.path.abspath(__file__))
    package_path = os.path.basename(package_path)
else:
    package_name = __package__
    package_path = os.path.dirname(os.path.abspath(__file__))



class Info:
    def __init__(self):
        self.multiplier = 10
        self.value = 1
    def showInfoList(self, multiplier, *args):
        for arg in args:
            print(arg * multiplier)

    def showInfoDict(self, **args):
        for key, value in args.items():
            print(f"{key} = {value}")


    def getValue(self, multiplier, value):
        self.value = value * multiplier
        return self.value;

    @classmethod
    def showValue(self):
        print(f"Value: {self.value}")

    def getValue(value):
        return value

    def showValue(value):
        print(value)