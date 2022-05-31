from deck import Deck

class Player:

    def __init__(self, name, deck, is_computer = False) -> None:
        self.name = name
        self._deck = deck #non public 
        self._is_computer = is_computer# non public should not change outside of the class 

    @property
    def is_computer(self):
        return self.is_computer

    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        return self._deck.size == 0

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)

