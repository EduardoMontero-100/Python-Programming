class Cake:

	def __init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality

my_cake = Cake('sugar', 130, 10)
print(f'The cake you just buy costed: {my_cake.price} dolars.')