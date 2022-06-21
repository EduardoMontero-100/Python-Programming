from typing import ItemsView


a = [1, 2, 3, 4]
b = a
c = b
d = c
## they are aliasing (different name, same objects)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
# all are referencing the same object
print(a is b is c is d)


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

print('Before')  
my_circle = Circle(4)
your_circle = my_circle
print(your_circle.radius)
print(my_circle.radius)


print('After')
your_circle.radius = 8
print(your_circle.radius)
print(my_circle.radius)

class Backpack:

    def __init__(self) -> None:
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_items(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print(f'The item {item} is not in the backpack')


my_backpack = Backpack()
your_backpack = my_backpack
her_backpack = your_backpack

print(my_backpack is your_backpack is her_backpack)
my_backpack.add_items('Water Bottle')
my_backpack.add_items('Candy')

print(my_backpack.items)
print(your_backpack.items)
print(her_backpack.items)

her_backpack.remove_item('Candy')


print(my_backpack.items)
print(your_backpack.items)
print(her_backpack.items)

#bugs generated with a mutuble objects
def add_absolute_values(seq):
    total = 0
    for i in range(len(seq)):
        seq[i] = abs(seq[i])
    return sum(seq)

seq = [-5,-6,-7,-8]

print(f'Values Before: {seq}')
add_absolute_values(seq)
print(f'Values After: {seq}')

a = (1,2,3,4,5)
a[:2]

# we got a runtime error. The dictionary size change during iteration
def remove_even_values(dictionary):
    for key, value in dictionary.items():
        if value %2 == 0:
            del dictionary[key]

my_dictionary = {'a': 1,
                 'b': 2,
                 'c': 3,
                 'd':4
               }

remove_even_values(my_dictionary)


a = [90,2,8,5]
print(a)
a.sort()
print(a)

print('xxxxxxxxxxxxx')
a = [90,2,8,5]
print(a)
b = sorted(a)
print(b)

##########################################################################################################################
# Cloning: creating a copy of the object totally independent from the original
#######################################################################################################################
a = [1,2,3,4]
b = a

b = a[:]
b[0] =15
print(a)
print(b)


# we got a runtime error. The dictionary size change during iteration
# Solved using clones
def remove_even_values(dictionary):
    for key, value in dictionary.copy().items():
        if value %2 == 0:
            del dictionary[key]

my_dictionary = {'a': 1,
                 'b': 2,
                 'c': 3,
                 'd':4
               }
print(my_dictionary)
remove_even_values(my_dictionary)
print(my_dictionary)





