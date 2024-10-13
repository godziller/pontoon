from brlapi import rangeType_key
from gi.overrides.keysyms import value

from Card import Card

class PontoonCard(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self._value = self.get_value()

    def get_value(self):
        face_cards = ["J",'Q','K']
        if self._rank in face_cards:
            return 10
        elif self._rank == "A":
            return 11
        else:
            return int(self._rank)

    def __str__(self):
        return f"Its value its [{self._value}]"

if __name__ == "__main__":
    my_P_card = PontoonCard("Spades", "3")
    print(my_P_card.get_value())
    print(my_P_card)
    #print(my_card)