

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(1.5,5555,868,9999))


def calculate(n, **kwargs):
    for key, value in kwargs.items():



calculate(2, add= 3, multiply = 5)

class Car():
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="VW", model = "Polo")
