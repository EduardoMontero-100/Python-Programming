""" from random import randint


class Die:

    def __init__(self, value) -> None:
        self.value = value 

    def roll_die(self):
        self.value = randint(1,6)

    
my_die = Die(4)
print(my_die.value)
my_die.roll_die()
print(my_die.value) """


""" from math import pi

class Circle:
    
    def __init__(self, radius) -> None:
        self.radius = radius

    def find_area(self, radius):
        return self.radius**2 * pi """


from math import *

print(pi)
print(sin(50))
print(cos(50))