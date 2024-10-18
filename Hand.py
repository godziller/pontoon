from PontoonCard import PontoonCard
#obj: add one card to hand

class Hand(object):

    def __init__(self):
        self._handlist = []
        self._value = 0

    def add_card(self, card):
        self._handlist.append(card)
        self._value += card.value

    def get_value(self):
        return self._value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "\n".join(str(card) for card in self._handlist)


if __name__ == "__main__":
    my_hand = Hand()
    my_hand.add_card(PontoonCard("Hearts","A"))
    print(my_hand.get_value())

    my_hand.add_card(PontoonCard("Diamonds","3"))
    print(my_hand.get_value())

    my_hand.add_card(PontoonCard("Hearts","K"))
    print(my_hand.get_value())

    print(my_hand)