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