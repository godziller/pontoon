# Student Number: 123411792
from Card import Card

class PontoonCard(Card):
    def __init__(self, suit, rank):
        """
        PontoonCard is a subclass of Card.

        The specialization in this class is related to the value assigned to a card.
        Number cards have their numerical value
        The Ace card is assigned a value of 11
        All other picture cards are assigned a value of 10
        :param suit: the suit of the car
        :param rank: the rank of the card
        """

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