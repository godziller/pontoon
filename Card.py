
class Card(object):

    #old_suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    #suit_list = ['\u2663', '\u2660', '\u2666', '\u2665']  # Clubs, Spades, Diamonds, Hearts
    rank_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = {
        'Clubs': '\u2663',
        'Spades': '\u2660',
        'Diamonds': '\u2666',
        'Hearts': '\u2665'
    }


    def __init__(self, in_suit, in_rank):
        """
           The Card constructor takes in the suit and the rank of the card to create

           A Card has no concept of 'value' as different games may assign different values to a card.
           It is expected a subclass of this type will set the value. Here we set it to 0 to reflect this.
           This allows this class to supply a reusable getter for value

           :param in_suit: the suit of the card
           :param in_rank: the rank of the card
           """

        # Check if the input suit is a full name or a symbol
        if in_suit in self.suits:
            self._suit = self.suits[in_suit]  # Convert full name to symbol
        else:
            raise ValueError("Invalid Suit")

        self._rank = in_rank
        self._value = 0         #default 0, expect subclasses to set correct value

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    #^^ above im showing the old method ^^

    #in this class below im showing the new getter method of getting a class property
    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def __str__(self):
        #return f"the {self._rank} of {self._suit}" - old print for long strings
        return f"{self._rank}{self._suit}"


if __name__ == "__main__":
    suit = 'Spades'
    junk = 'Junk'
    rank =  "K"

    try:
        my_card = Card(suit, rank)
    except:
        print(f"Invalid Suit: {suit}")

    try:
        my_card = Card(junk, rank)
    except:
        print(f"Invalid Suit: {junk}")
    #validating rank




