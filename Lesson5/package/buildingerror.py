
class BuildingError(Exception):

    def __str__(self,value):
        return value

    def check(self, amount, limit):
        if(amount <= limit):
            return True
    else:
        error = f"{amount}is greater then {limit}"
        raise BuildingError(self, error)
