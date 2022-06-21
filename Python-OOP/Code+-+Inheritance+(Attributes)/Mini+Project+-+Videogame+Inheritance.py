class Sprite:
    
	def __init__(self, x, y, img_file, speed, life_counter):
		self.x = x
		self.y = y
		self.img_file = img_file
		self.speed = speed
		self.life_counter = life_counter

class Enemy(Sprite):
    
	MESSAGE = "I'm here to protect my master"

	def __init__(self, x, y, img_file, speed, life_counter):
		Sprite.__init__(self, x, y, img_file, speed, life_counter=5)


class Player(Enemy):
    
	def __init__(self, x, y, img_file, speed=56, life_counter=6):
		Sprite.__init__(self, x, y, img_file, speed, life_counter)


class DifficultEnemy(Enemy):
    
	def __init__(self, x, y, img_file):
		Enemy.__init__(self, x, y, img_file, speed, life_counter)


class EasyEnemy(Player):
    
	def __init__(self, x, y, img_file, speed, life_counter):
		Enemy.__init__(self, x, y, img_file, speed, life_counter)
		self.life_counter = 1
