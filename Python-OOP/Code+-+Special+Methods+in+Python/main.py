""" result = 5 + 6
print(result)

result = (5).__add__(6)
print((5).__add__(6)) """


class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


#my_point = Point2D(4,5)
#print(my_point)


class Student:

    def __init__(self, student_id, name, age, gpa) -> None:
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self) -> str:
        return f'Student: {self.name} |'\
               f'Student ID : {self.student_id} |'\
               f'Student Name: {self.name} |'\
               f'Student Age: {self.age} |'\
               f'Student GPA: {self.gpa}'
        
my_student = Student('SA123', 'Eduardo Montero', 25, 120 )
print(my_student)

print('---------String Len-------------')
my_string = "Hello, World!"
print(len(my_string))
print(my_string.__len__())

print('----------List Len------------')
my_list = [1,2,3,4,5]
print(len(my_list))
print(my_list.__len__())

print('----------Tuple Len------------')
my_tuple = (1,2,3,4,5)
print(len(my_list))
print(my_tuple.__len__())


print('----------Dictionary------------')
my_dictionary= {'a':1, 'b':2, 'c':3}
print(len(my_dictionary))
print(my_dictionary.__len__())


print('----------Backpack------------')
class Backpack:

    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'The item {item} is not in the list of items')

    def __len__(self):
        return len(self.items)

my_backpack = Backpack()
my_backpack.add_item('Candy')
my_backpack.add_item('Water Bottle')
my_backpack.add_item('Sleeping Back')

print('-----------------------------')
print('My Backpack')
print(len(my_backpack))
my_backpack.remove_item('Candy')
print(len(my_backpack))
