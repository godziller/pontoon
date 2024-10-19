from Hand import Hand
from PontoonCard import PontoonCard

class Player(object):

    def __init__(self, in_name):
        self._name = in_name
        self._hand = Hand()     #Player HAS A hand


    @property
    def hand(self):
        return self._hand



    def __str__(self):
        return self._name


if __name__ == "__main__":

    my_player = Player("Darren")
    print(my_player)
    print(my_player.hand.value)
    new_card = PontoonCard("Hearts", "Q")
    my_player.hand.add_card(new_card)
    print(my_player.hand.value)
