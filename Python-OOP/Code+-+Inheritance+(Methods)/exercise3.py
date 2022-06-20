from numpy import full


class Store:
    
    def __init__(self, full_name, store_id) -> None:
        self.full_name = full_name
        self.store_id = store_id

    def greet_customers(self):
        return 'Welcome to the store!'

class DonutStore(Store):
    
    def greet_customers(self):
        return Store.greet_customers(self) + '\n' + f'This store, {self.full_name} it the best.'



my_donut_store = DonutStore('DrugStore','123A431')
print(my_donut_store.greet_customers())

