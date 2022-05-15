#class Dog:
#    #Class attributes
#    species = 'Canis familiaris'  
#    # __init__() method
#    def __init__(self, name, age, breed):
#        self.name = name
#        self.age = age
#        self.breed = breed
#
#class Backpack:
#    #Class attributes
#    max_num_items = 10
#    # __init__() method
#    def __init__(self):
#        self.items =[]
#class Quadruped:
#    
#    num_feet=4
#
#    def __init__(self, flies) -> None:
#        self.flies=flies
#
#
#my_quadruped = Quadruped(True)
#
#print(f'Your quadrupe flies? {my_quadruped.flies}')
#print(f'How many feet your animal has? {my_quadruped.num_feet}')
#print(f'How many feet your animal has? {Quadruped.num_feet}')
#
## Creating an Id to a instance based on class attribute
#class Movie:
#
#    id_counter = 1
#
#    def __init__(self, title, rating) -> None:
#        self.id = Movie.id_counter
#        self.title = title
#        self.rating = rating
#
#        Movie.id_counter+=1
#
#
#my_movie = Movie('Titanic', 4.7)
#your_movie = Movie('Lord of the Rings', 4.9)
#
#
#print(f'Titanic Id {my_movie.id}')
#print(f'Lord of the Rings Id {your_movie.id}')
#
#class Backpack:
#
#    max_num_items = 10
#
#    def __init__(self) -> None:
#        self.items =[]
#        
#
#my_backpack = Backpack()
#your_backpack = Backpack()
#
#print(Backpack.max_num_items)
#
#print(my_backpack.max_num_items)
#print(your_backpack.max_num_items)
#class MyEditorialBook:
#
#    has_cover = True
#    editorial_code = 4531
#
#    def __init__(self,title, number_pages, published) -> None:
#        self.title = title
#        self.number_pages = number_pages
#        self.published = published
#
#    
#cover =  MyEditorialBook.has_cover
#code = MyEditorialBook.editorial_code
#class Circle:
#
#    radius = 5
#
#    def __init__(self, color) -> None:
#        self.color = color
#
#
#print(Circle.radius)
#
#my_circle = Circle('Blue')
#your_circle = Circle('Green')
#
#print(my_circle.radius)
#print(your_circle.radius)
#
#Circle.radius = 20
#
#print(Circle.radius)
#print(my_circle.radius)
#print(your_circle.radius)
#class Pizza:
#
#    price = 12.99
#
#    def __init__(self, description, toppings, crusts) -> None:
#        self.description = description
#        self.toppings = toppings
#        self.crusts = crusts
#
#
#print(Pizza.price)
#
#my_pizza = Pizza('Margherita', ['Basil', 'Mushrooms'], 'New York Style')
#print(my_pizza.price)
#        
#
#Pizza.price= 15.99
#
#print(Pizza.price)
#print(my_pizza.price)
#
#
#class Backpack:
#
#    max_num_items = 10
#
#    def __init__(self) -> None:
#        self.items = []
#
#print(Backpack.max_num_items)
#
#my_backpack = Backpack()
#print(my_backpack.max_num_items)
#
#Backpack.max_num_items =30
#
#print(Backpack.max_num_items)
#print(my_backpack.max_num_items)
#

