from numpy import full


class Polygon:
    
    def __init__(self, num_sides, color) -> None:
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f'This polygon has {self.num_sides} and it is {self.color}.')

    
class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color) -> None:
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height

    def find_area(self):
        return self.base * self.height/2

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self, side_length, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_length = side_length
        
    def find_area(self):
        return self.side_length**2

""" my_triangule= Triangle(5,4, 'red')
my_triangule.describe_polygon()
print(my_triangule.find_area())


my_square = Square(6, 'green')
my_square.describe_polygon()
print(my_square.find_area())
 """

class Teacher:

    def __init__(self, full_name, teacher_id) -> None:
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        return f'Welcome dear students! I am your teacher. My name is {self.full_name}'

class ScienceTeacher(Teacher):

    def welcome_students(self):
       # return f'Science is amazing! \n' + Teacher.welcome_students(self) 
        return f'Science is amazing! \n' + super().welcome_students() 


my_science_teacher = ScienceTeacher('Eduardo Montero', 'S123A324')
print(my_science_teacher.welcome_students())



