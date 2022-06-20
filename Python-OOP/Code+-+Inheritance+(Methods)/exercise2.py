class Backpack:
    
    def __init__(self) -> None:
        self.items = []

    def add_snack(self, snack):
        print(f'Adding a new snack')
        self.items.append(snack)
        print(f'{snack} was added successfully')


class SchoolBackpack(Backpack):
    
    def add_snack(self, snack):
        print('It is time to go to school. Lets add an snack')
        Backpack.add_snack(self, snack)
        print(f'Now your backpack has the items {self.items}')

my_backpack = SchoolBackpack()
my_backpack.add_snack('Candy')
my_backpack.add_snack('Bubble Gum')