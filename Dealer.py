from Player import Player


class Dealer(Player):
    def __init__(self, playing_deck):
        super().__init__("Dealer")
        self._deck = playing_deck

    def play_out(self, count_to_beat):
        '''
        Play_out method takes in an int representing the highest
        count at the table. This is the target the Dealer has
        to beat.
        '''
        # The logic of a player hitting is to remove a card object from
        # -the deck and add it to the players hand.
        dealer_value = self.hand.value     #dealers current hand value.#
        while dealer_value <= count_to_beat:
            hit_card = self._deck.deal_card()
            self.hand.add_card(hit_card)
            dealer_value = self.hand.value      # As long as the dealers value is less or equal to the highest
                                                # players amount, hit perpetually until bust.
        return dealer_value


if __name__ == "__main__":
    ...
    #my_dealer = Dealer()
    #print(my_dealer)
