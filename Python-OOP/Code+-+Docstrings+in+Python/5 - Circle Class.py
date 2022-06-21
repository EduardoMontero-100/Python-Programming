"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

import math


class Circle:
    """A class that represents a circle.

    Attributes:
        radius (float): the distance from the center of the circle to its circumference.
        color (string); the color of the circle.
        diameter (float): the distance through the center of the circle from one side
        to the other.

    Methods:
        find_area(self):
            Return the area of the circle.
        find_perimeter(self):
            Return the perimeter of the circle.
    """
    def __init__(self, radius, color):
        """Initialize an instance of Circle.

        Arguments:
            radius (float): the distance from the center
                of the circle to its circumference.
            color (string): the color of the circle. 
        """
        self.__radius = radius
        self.__color = color

    @property
    def radius(self):
        """ Return the radius of the circle. 
        
        This is a float tha represents the distance from the center
        of the circle to its circumference."""
        return self.__radius

    @property
    def color(self):
        """Return the color of the circle represented as a string.

        The color is described by a string that must be capitalized.
        For example: "Red", "Blue", "Green", "Yellow". 
        """
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    @property
    def diameter(self):
        """Return the diameter of the circle.

        This is a float that represents the distance through the center of
        the circle from one side to the other. 
        """
        return 2 * self.__radius

    def find_area(self):
        """Find and return the area of the circle.

        The area is calculated with the circle radius 
        using the formula Pi * (radius ** 2).
        """

        return math.pi * (self.__radius ** 2)

    def find_perimeter(self):
        """Find and return the perimeter of the circle.

        The perimeter is calculated with the circle radius
        using the formula (2 * Pi * radius) 
        """
        return 2 * math.pi * self.__radius


print(Circle.__doc__)
print(help(Circle))