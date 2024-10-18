from Player import Player


class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def play_out(self, count_to_beat):
        '''
        Play_out method takes in an int representing the highest
        count at the table. This is the target the Dealer has
        to beat.
        '''
        ...


if __name__ == "__main__":
    my_dealer = Dealer()
    print(my_dealer)
