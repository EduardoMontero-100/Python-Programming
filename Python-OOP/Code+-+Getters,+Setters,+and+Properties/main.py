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

from lib2to3.pgen2.token import CIRCUMFLEX
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


class Dog:

    def __init__(self, age) -> None:
        self._age = age

    def get_age(self):
        print('Calling the getter')
        return self._age

    def set_age(self, new_age):
        print('Calling the setter')
        if isinstance(new_age, int) and 0 < new_age <30:
            self._age = new_age
        else:
            print('Please enter a valid age')

    age = property(get_age, set_age)

my_dog = Dog(4)

print(f'My dog is {my_dog.age} years old')
print('One year later...')

my_dog.age+=1
print(f'My dog is new {my_dog.age} years old')
