# version with property sintax
class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        print('Calling getter price...')
        return self._price
    
    def set_price(self, new_price):
        print('Calling setter price...')
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price
        else:
            print('Please enter a valid value')

    price = property(get_price, set_price)    

my_bouncyball = BouncyBall(222, 2, 'new')

print(my_bouncyball.price)
my_bouncyball.price=333.0
print(my_bouncyball.price)

# version with property sintax

class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    # version with @property sintax
    @property
    def price(self):
        print('Calling getter price...')
        return self._price
    
    @price.setter
    def price(self, new_price):
        print('Calling setter price...')
        if new_price > 0:
            self._price = new_price
        else:
            print('Please enter a valid value')

my_bouncyball = BouncyBall(222, 2, 'new')
print(my_bouncyball.price)
my_bouncyball.price=333
print(my_bouncyball.price)

    


           


        