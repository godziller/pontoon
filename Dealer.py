# Student Number: 123411792
from Player import Player

class Dealer(Player):
    def __init__(self, playing_deck):
        """
        THe Dealer class is a subclass of Player.

        This class adds specialized functionality specific to a Dealer.
        The constructor takes in an instance of a playing deck to allow the Dealer instance to operator on that.

        :param playing_deck: an instance of a created playing deck
        """

        super().__init__("Dealer")
        self._deck = playing_deck

    def play_out(self, count_to_beat):
        """
        play_out instructs the dealer instance to attempt to beat the count_to_beat integer.

        This function is typically called when call the players have had their turn at the game.
        count_to_beat represents the current round's highest hand held.
        play_out will either succeed in beating this or going bust.
        The user of this function will understand a return value greater than 21 implies bust.

        :param count_to_beat: Integer representing the hand count at the table to beat.
        :return: The Dealers Hand value after attempting to beat this.
        """
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
