class Professor:
    
    def __init__(self, name, age, course, num_subjects) -> None:
        self.name = name
        self.age = age
        self.course = course
        self.num_subjects = num_subjects

    def greet_students(self):
        return 'Welcome to the University'

class ScienceProfessor(Professor):
    
    NUM_SUBJECTS =4

    def __init__(self, name, age, course, is_enginneer):
        Professor.__init__(self,name, age, course, ScienceProfessor.NUM_SUBJECTS)
        self.is_enginneer = is_enginneer

    def greet_students(self):
        return 'Hi everyone! It is a great day to study science '#+ '\n'+super().greet_students()

Eduardo = ScienceProfessor('Eduardo', 34, 'Programming', True)
print(Eduardo.greet_students())
