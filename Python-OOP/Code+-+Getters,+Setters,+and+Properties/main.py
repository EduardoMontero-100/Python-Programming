#class Movie:
#
#    def __init__(self, title, rating) -> None:
#        self._title = title #non-public
#        self.rating = rating
#
#    def get_title(self): #It is like an intermediate process
#        return self._title
#
#    
#my_movie = Movie('The GodFather', 4.8)
##
##print(f'My favorite movie is {my_movie.get_title()}')
#
#class Dog:
#
#    def __init__(self, name, age) -> None:
#        self._name = name # non-public attribute
#        self.age = age
#
#    def get_name(self):
#        return self._name
#
#    def set_name(self, new_name):
#        # verifica si el nuevo nombre es un objeto de la clase string y si es alfabetico
#        if isinstance(new_name, str) and new_name.isalpha():
#            self._name = new_name
#        else:
#            print('Please enter a valid name')
#
#
#my_dog = Dog('Nora', 8)
#
#print(f'My dog is {my_dog.get_name()}' )
#
#my_dog.set_name('Norita')
#
#print(f'My dog is new {my_dog.get_name()}')

#class Backpack:
#
#    def __init__(self) -> None:
#        self._items = []
#
#    def get_items(self):
#        return self._items
#
#    def set_items(self, new_items):
#        if isinstance(new_items, list):
#            self._items = new_items
#        else:
#            print('Please enter a valid list of items.')
#
#my_backpack = Backpack()
#print(my_backpack.get_items())
#
#my_backpack.set_items(['Water Bottle', 'Sleeping Bag', 'First Aid Kit'])
#print(my_backpack.get_items())

#my_backpack.set_items('Hello World')
#print(my_backpack.get_items())
#
#
#class Circle:
#
#    def __init__(self,radius) -> None:
#        self._radius = radius
#
#    def get_radius(self):
#        return self._radius
#
#    def set_radius(self, new_radius):
#        if isinstance(new_radius, float) and new_radius>0:
#            self._radius = new_radius
#        else:
#            print('Please enter a valid value')
#
#my_circle = Circle(5.6)
#print(f'The radius of the circle is: {my_circle.get_radius()}')
#
#my_circle.set_radius(6.9)
#print(f'The new radius of the circle is: {my_circle.get_radius()}')
#
#my_circle.set_radius('Hello world')
#print(f'The new radius of the circle is: {my_circle.get_radius()}')
#

#
#class Dog:
#
#    def __init__(self, age) -> None:
#        self._age = age
#
#    def get_age(self):
#        print('Calling the getter')
#        return self._age
#
#    def set_age(self, new_age):
#        print('Calling the setter')
#        if isinstance(new_age, int) and 0 < new_age <30:
#            self._age = new_age
#        else:
#            print('Please enter a valid age')
#
#    age = property(get_age, set_age)
#
#my_dog = Dog(4)
#
#print(f'My dog is {my_dog.age} years old')
#print('One year later...')
#
#my_dog.age+=1
#print(f'My dog is new {my_dog.age} years old')
#

## Properties
#
#class Circle:
#
#    VALID_COLORS = ("Red", "Blue", "Green")# Class constant
#
#    def __init__(self, radius, color) -> None:
#        self._radius = radius # it is a non public attribute
#        self._color = color # it is a non public attribute
#
#    def get_radius(self):
#        return self._radius
#
#    def set_radius(self, new_radius):
#        if new_radius > 0 and isinstance(new_radius, int):
#            self._radius = new_radius
#        else:
#            print('Please insert a valid radius')
#    
#    radius = property(get_radius,set_radius)
#
#    def get_color(self):
#        return self._color
#
#    def set_color(self, new_color):
#        if new_color in Circle.VALID_COLORS:
#            self._color=new_color
#        else:
#            print('Please insert a valid color')
#
#    color = property(get_color, set_color) # is a way to protect the attribute from outside
#
#
#my_circle = Circle(5, 'Red')
##Color:
##print(my_circle._color)
#my_circle.color = 'Black' # Calling the name of the property
#print(my_circle._color)

#Radius
#print(my_circle.radius)
#my_circle.radius=90 # Calling the name of the property
#print(my_circle.radius) 


#from curses.ascii import isalpha
#
#
#class Movie:
#
#    def __init__(self, title, rating) -> None:
#        self.title = title
#        self._rating = rating
#
#    ## Getter using @property
#    @property
#    def rating(self): # the name of the property
#        print('Calling the getter...')
#        return self._rating # the name of the non-public attribute
#
#    ## Setter using @property_name (@rating)
#    @rating.setter
#    def rating(self, new_rating):
#        print('Calling the setter...')
#        if 1.0 <= new_rating <= 5.0 and isinstance(new_rating, float):
#            self._rating = new_rating
#        else:
#            print('Please enter a valid rating')
#
##Test getters and setters
#my_movie = Movie('Titanic', 4.3)
#print(my_movie.rating)
#
#my_movie.rating=-5
#print(my_movie.rating)
#


class Backpack:

    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):# Getter. It has the name of the property we want to create
        print('Calling the getter...')
        return self._items

    @items.setter # Setter
    def items(self, new_items):
        print('Calling the setter...')
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please, enter a valid list')
    
my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items=['notebook', 'laptop', 'pencil']
print(my_backpack.items)        