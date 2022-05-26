



#my_list = [4, 5, 6, 7, 8]
#
#my_list.sort()
#print(my_list)
#
#my_list.append(14)
#print(my_list)
#
#my_list.extend([1, 2, 3])
#print(my_list)
#
#number = my_list.pop()
#print(number)
#print(my_list)


#class Circle:
#
#    def __init__(self, radius) -> None:
#        self.radius = radius
#    #define a method
#    def find_diameter(self):
#        return self.radius * 2     
#
#my_circle = Circle(5)
#diameter = my_circle.find_diameter()
#print(diameter)



#class Player:
#
#    def __init__(self, x, y) -> None:
#        self.x = x
#        self.y = y
#
#    def move_up(self, change=5):
#        self.y += change
#
#    def move_down(self, change=5):
#        self.y -= change
#    
#    def move_right(self, change=2):
#        self.x += change
#
#    def move_left(self, change=2):
#        self.x -= change
#    
#my_player = Player(5,10)
#print(my_player.x)
#my_player.move_left(10)
#print(my_player.x)




class Backpack:

    def __init__(self) -> None:
        self._items = []
    #getter
    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Please enter a valid item.')

    def remote_item(self, item):
        if item in self._items:
            self.items.remove(item)
            return 1 # indicate that the operation was successfull
        else:
            print('This item is not included in the list of items')
            return 0 # indicate that the operation was no successfull

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            return print(sorted(self._items))
        else:
            return print(self._items)
        
my_backpack = Backpack()
print(my_backpack.items)
my_backpack.add_multiple_items(['Water Bottle', 'Candy'])
print(my_backpack.items)




my_backpack.add_item('Water Bottle')
my_backpack.add_item('Sleeping Bag')
my_backpack.add_item('Candy')

print('Not Sorted:')
my_backpack.show_items()

print('Sorted:')
my_backpack.show_items(True)




my_backpack = Backpack()
print(my_backpack._items)

my_backpack.add_item('Water Bottle')
print(my_backpack._items)

my_backpack.add_item('Sleeping Bag')
print(my_backpack._items)

has_water = my_backpack.has_item('Water Bottle')
print(has_water)

my_backpack.remote_item('Water Bottle')
print(my_backpack._items)
my_backpack.remote_item('Sleeping Bag')
print(my_backpack._items)

my_backpack.remote_item('Candy')
print(my_backpack._items)