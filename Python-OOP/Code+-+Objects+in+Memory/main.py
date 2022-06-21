from opcode import HAVE_ARGUMENT


print(object)
print(isinstance(5, object))
print(isinstance(list, object))
print(isinstance('Hello world!', object))
print(isinstance({'a':5, 'b':6}, object))
print(isinstance(True, object))


def f(x):
    return x * 2

print(isinstance(f, object))
# funtions are objects as well

class Movie:

    def __init__(self, title) -> None:
        self.title = title


print(isinstance(Movie, object))

# Everything in python is an object integers, floats, tuples, etc.
# When you create an object, it is stored in memory base on an id (memory location)

a = [1,2,3,4,5]
b = [5,4,3,2,1]

# Reference: name that refers to the location in memory of an object:
    # variables, attributes, items (used them to access an object)
    # variables: In python store references to objects in memory
    # the variable knows where to get the object in memory

# Garbage Collection: Objects that are not used are deleted from memory (automatic process)

# Object vs. Instance:
#But you can think of objects as the "physical" existence of the instances in memory, the data that is stored in memory to represent the instances, while instances represent a more theoretical concept. A specific house object represents an instance of the House class in memory.


a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(id(a))
print(id(b))

print(id(a)) # returns the address of the object in memory

print(id(15))
print(id('Hello World!'))


class Backpack:

    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):
        return self._items

my_backpack= Backpack()
your_backpack= Backpack()

print(id(my_backpack))
print(id(your_backpack))

## is Operator
#If two variables do not reference the same object, they will have different ids

# two variables reference the same object
a = [4,3,2,3]
b = a
print(id(a))
print(id(b))

# "is" vs. ==
# is ==> Checks the objects
# == Checks the values of the objects

# two objects may have the same value and still be differents objects in memory:

a = [2,3,2]
b = [2,3,2]

print(id(a))
print(id(b))

print(a is b)
print(a == b)

a = [1,2,3,2]
b = [3,4,2,3]

print(a is b)
print(b is a)

b = a
print(a is b)

e = "Hello, World!"
p = "Hello, World!"

print(e is p)
print(p is e)

###################################################
# Unexpected results in small integers [-5, 256]
# The same happens in 
###################################################
a = -5
b = -5

print(a is b)

a = -6
b = -6

print(a is b)

a = 257
b = 257
print(a is b)

#All of the have same object location
a = 'Hi'
print(id(a))

b = 'Hi'
print(id(b))

c = 'Hi'
print(id(c))

d = 'Hi'
print(id(d))

print(a is b is c is d)

##################################################
# Objects can be pass by value or by reference
##################################################

# In Python, objects are passed by reference

my_list = [2,1,3,4]

def print_data(seq):
    print(f'Inside the function {id(seq)}')
    for elem in seq:
        print(elem)

print(f'Outside the function {id(my_list)}')
print_data(my_list) # This element is passed by reference

# We are refering to the same object in memory
# Is like que are passing the id    
# When both variables refere the same object in memory


my_list =[6, 2, 8 , 2]


def multiply_by_two(seq):
    print(f'Inside the function {id(my_list)}')
    for i in range(len(seq)):
        seq[i]*=2

print(f'Outside the function {id(my_list)}')
multiply_by_two(my_list)
############################################
## Working with Objects
############################################
class Sales:

    def __init__(self, amount) -> None:
        self.amount = amount


def find_total(sales):
    total = 0

    for sale in sales:
        print('New sale...')
        print(sale.amount)
        total += sale.amount

    return total

january_sales = [Sales(400), Sales(345), Sales(45)]
print(find_total(january_sales))


############################################






x = 'abc'
y = 'abc'
x is y 
print(id(x))
print(id(y))


############################################
a  = [1,2,3,4]
b = [1,2,3,4]

print(id(a))
print(id(b))

print(a is b)
print(a == b)
############################################

a =[1,2,3,4]
b =[3,4,2,1]

print(a is b)

a =[1,2,3,4]
b = a

print(a is b)
############################################
