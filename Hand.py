from PontoonCard import PontoonCard
#obj: add one card to hand

class Hand(object):
    """
    The Hand Class represent a Player's hand.

    The Hand class will contain a number of cards and a value. The value is the cumulative count of all cards held by the hand.
    """

    def __init__(self):
        self._handlist = []
        self._value = 0

    def add_card(self, card):
        """
        add_card adds a card object to a hand instance

        Along with adding a card, the value of the added card is added to the hand value on this call
        :param card:
        :return:
        """
        self._handlist.append(card)
        self._value += card.value

    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)


    def __str__(self):
        return ", ".join(str(card) for card in self._handlist)


if __name__ == "__main__":
    my_hand = Hand()
    my_hand.add_card(PontoonCard("Hearts","A"))
    print(my_hand.get_value())

    my_hand.add_card(PontoonCard("Diamonds","3"))
    print(my_hand.get_value())

    my_hand.add_card(PontoonCard("Hearts","K"))
    print(my_hand.get_value())

    print(my_hand)