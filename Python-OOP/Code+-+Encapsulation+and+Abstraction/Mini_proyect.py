class Book:
    """
    Mini proyect
    """
    def __init__(self, title, author, num_pages, ISBN, publisher) -> None:
        self.title = title
        self.author = author
        self._num_pages = num_pages
        self._ISBN=ISBN
        self._publisher = publisher

my_book = Book('Scary Movie', 'Homero', 50, 'GTGUH8988', 'Casa Rosada')
print(my_book._num_pages)