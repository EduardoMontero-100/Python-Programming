class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        #self.color = color
        self.color = 'Blue'

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class House:
    def __init__(self, price): #self refers to the instance
        self.price = price # price parameter is assigned to price attibute


class Backpack:

    def __init__(self,): #permite definir los atributos de la instancia
        self.items =[]

# creating an instances that does not need an argument
my_backpack = Backpack()
print(my_backpack)

# Create an instance when one argument is requered
class Circle:
    def __init__(self, radius):
        self.radius = radius


my_circle = Circle(5)
print(my_circle)


# Create an instance when more than one argument is requered
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width= width


my_rectangle = Rectangle(5, 4)
print(my_rectangle)

class Dog:

    def __init__(self, name, age, color, is_male):
        self.name = name
        self.age = age
        self.color = color
        self.is_male = is_male


my_dog = Dog('Pepe', 2, 'black', True)
print(my_dog)

