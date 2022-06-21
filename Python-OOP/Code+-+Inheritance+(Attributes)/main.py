from pickle import TRUE
from numpy import full


class Polygon:

    def __init__(self, num_sides, color) -> None:
        self.num_sides = num_sides
        self.color = color

    def __str__(self) -> str:
        return 'Es un triangulo'


class Triangle(Polygon):
    
    NUM_SIDES = 3

    def __init__(self,base, height, color) -> None:
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height




class Square(Polygon):
    pass

#print(f'Square is a Polygon? {issubclass(Square, Polygon)}')


#my_triangle = Triangle(10, 50, 'blue')
#print(f'{my_triangle}')
#print(my_triangle.base)
#print(my_triangle.height)
#print(my_triangle.num_sides)
#print(my_triangle.color)


class Employee:

    def __init__(self, full_name, salary) -> None:
        self.full_name = full_name
        self.salary = salary

    
class Programmer(Employee):

    def __init__(self, full_name, salary, programming_language) -> None:
        #super().__init__(full_name, salary)
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


Nora = Programmer('Nora', 60000, 'Python')
#print(Nora.full_name)
#print(Nora.salary)
#print(Nora.programming_language)

class Character:
    
    def __init__(self, x, y, num_lives) -> None:
        self.x = x
        self.y = y
        self.num_lives = num_lives
        
    

class Player(Character):

    INITIAL_X = 0
    INIITAL_Y = 0
    INITIAL_NUM_LIVES = 10

    def __init__(self, score =0) -> None:
        Character.__init__(self, Player.INITIAL_X, Player.INIITAL_Y, Player.INITIAL_NUM_LIVES)
        self.score = score

class Enemy(Character):
    

    def __init__(self, x=15, y=15, num_lives=8, is_poisonous = False):
        Character.__init__(self, x, y, num_lives)
        self.is_poisonous = is_poisonous


""" my_player = Player()
print(my_player.score)
print(my_player.x)
print(my_player.y)
print(my_player.num_lives)
 """

easy_enemy = Enemy(num_lives=1)
hard_enemy = Enemy(num_lives=56, is_poisonous=True)


""" print(easy_enemy.is_poisonous)
print(easy_enemy.x)
print(easy_enemy.y)
print(easy_enemy.num_lives)
 """

""" print(hard_enemy.is_poisonous)
print(hard_enemy.x)
print(hard_enemy.y)
print(hard_enemy.num_lives) """


class Mammal:
    def __init__(self, name, age, health) -> None:
        self.name = name
        self.age = age
        self.health = health
        

class Panda(Mammal):

    IS_ENDANGERED = True
    def __init__(self, name, age, health) -> None:

        Mammal.__init__(self, name, age, health)

my_panda = Panda('Pepe', 5, 'is Ok')

print(my_panda.name)
print(my_panda.age)
print(my_panda.health)
print(my_panda.IS_ENDANGERED)

