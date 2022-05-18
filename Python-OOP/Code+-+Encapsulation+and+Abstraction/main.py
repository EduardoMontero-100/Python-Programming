
######################
## Encapsulation
######################
# Example of a public attribute
class Car:
    # those are public attibutes
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self.year = year


my_car = Car('Porche','911 Carrera', 2020)
print(my_car.year)
my_car.year = 5600
print(my_car.year)

# Example of a non-public attribute
class Car:
    # those are public attibutes
    def __init__(self, brand, model, year) -> None:
        self.brand = brand
        self.model = model
        self._year = year #non-public attribute


my_car = Car('Porche','911 Carrera', 2020)
print(my_car.year)
print(my_car._year)
# Example of a non-public attribute
class Student:

    def __init__(self, student_id, name, age, gpa) -> None:
        self.student_id = student_id
        self.name = name
        self._age = age # this attibute shouldn be access ==> no public attribute
        self.gpa= gpa


student_nora = Student('245FS', 'Nora Nav', 15, 3.96)
print(student_nora._age)
# Example of a non-public attribute
class Backpack:

    def __init__(self) -> None:
        self._items = []


my_backpack = Backpack()
print(my_backpack._items)
# Example of a non-public attribute
class Movie:

    id_counter = 1

    def __init__(self, title, year, language, rating) -> None:
        self._id= Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter+=1

my_movie = Movie('Pride and Prejudice', 2005, 'English', 4.7)
your_movie = Movie('Sense and Sensibility', 1995, 'English', 4.6)

print(my_movie._id)
print(your_movie._id)


class Backpack:
    
    def __init__(self) -> None:
        self.__items = ['Water Bottle','First Aid Kit']

my_backpack = Backpack()

#print(my_backpack.__items) # we cannot access the attribute with this way
print(my_backpack._Backpack__items) # this is the way. We can tecnically access but we shouldnt

