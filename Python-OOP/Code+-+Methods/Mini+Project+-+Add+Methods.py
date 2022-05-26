class MusicSchool:

	students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                "Talina": [28, "555-765-452", ["Chello"]],
                "Eric":   [12, "583-356-223", ["Singing"]]}

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

	# Add your methods below this line
	def print_student(self, name):
		if name in self.students.keys():
			print(f'Student: {name} who is {self.students[name][0]} years old and is taking {self.students[name][2]}')
		else:
			print('Please enter a valid name')

	def print_students_data(self):
		for key in self.students.keys():
			self.print_student(key)

	def add_student(self, name, attributes):
		self.students[name]=attributes

# Create the instance
my_music_school = MusicSchool(8, 15000)


# Call the methods
my_music_school.print_student('Gino')
print('-----------------------------------------------------------')
my_music_school.print_students_data()
print('-----------------------------------------------------------')
my_music_school.add_student('Jack', [60,'562-234-234', ['Piano']])
print('-----------------------------------------------------------')
my_music_school.print_students_data()
