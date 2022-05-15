from xml.sax.handler import feature_validation


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


# Accesing attributes inside the class
class Backpack:
    def __init__(self):
        self.items =[]
        print(self.items)


my_backpack=Backpack()


## Accesing attributes outside the class
class Backpack:
    def __init__(self):
        self.items =["Water Bottle", "Pencils"]
        print(self.items)


my_backpack=Backpack()
print(my_backpack.items)


class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_favorite_movie = Movie('Scare Movie', 2020, 'English', 4.8)
your_favorite_movie = Movie('Titanic', 1980, 'English', 4.2)

print('My favorite Movie:')
print('-----------------------------------------')
print(f'Title: {my_favorite_movie.title}')
print(f'Year: {my_favorite_movie.year}')
print(f'Language: {my_favorite_movie.language}')
print(f'Rating: {my_favorite_movie.rating}')



print('Your favorite Movie:')
print('-----------------------------------------')
print(f'Title: {your_favorite_movie.title}')
print(f'Year: {your_favorite_movie.year}')
print(f'Language: {your_favorite_movie.language}')
print(f'Rating: {your_favorite_movie.rating}')

# parameters with a default value must be at the end of the __init__ method
class Circle:
    def __init__(self, color, radius=5):
        self.color = color
        self.radius = radius


my_circle = Circle(7, 'Blue')
print(my_circle.radius)



## Modifing an instance attribute inside of the class
class Backpack:

    def __init__(self):
        self.items =[]


## Modifing an instance attribute outside of the class
class Backpack:

    def __init__(self, color):
        self.items =[]
        self.color = color

my_backpack = Backpack('Red')
your_backpack = Backpack('Blue')
print(f'The color of my backpack is {my_backpack.color}')
print(f'The color of your backpack is {your_backpack.color}')
print('Changing color....')
my_backpack.color='Green'
print(f'The color of my backpack is {my_backpack.color}')
print(f'The color of your backpack is {your_backpack.color}')




class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

my_circle = Circle(5, 'Red')

print('Inicial Attribute Values:')
print(my_circle.radius)
print(my_circle.color)

my_circle.radius = 15
my_circle.color = 'Black'
print('Changing Attribute Values:')
print(my_circle.radius)
print(my_circle.color)
