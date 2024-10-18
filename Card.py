
class Card(object):

    old_suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    suit_list = ['\u2663', '\u2660', '\u2666', '\u2665']  # Clubs, Spades, Diamonds, Hearts
    rank_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self, in_suit, in_rank):
        self._suit = in_suit
        self._rank = in_rank
        self._value = 0         #default 0, expect subclasses to set correct value

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank

    #^^ above im showing the old method ^^

    #in this class below im showing the new method of getting a class property
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
    rank =  "K"

    #Validating Suit
    try:
        if suit not in Card.suit_list:
            raise ValueError("Invalid Suit")
    except ValueError:
        print(f"Invalid Suit: {suit}")

    #validating rank
    try:
        my_card = Card(suit, rank)
        print(my_card)
        print(my_card.rank)
        print(my_card.value)

    except ValueError:
        print(f"Invalid Rank: {rank}")
    #print(my_card)


