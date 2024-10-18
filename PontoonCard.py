
from Card import Card

class PontoonCard(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

        self._value = self._calc_value()

    def _calc_value(self):
        face_cards = ["J",'Q','K']
        if self._rank in face_cards:
            return 10
        elif self._rank == "A":
            return 11
        else:
            return int(self._rank)


if __name__ == "__main__":
    my_P_card = PontoonCard("Spades", "A")
    print(my_P_card)
    print(my_P_card.value)