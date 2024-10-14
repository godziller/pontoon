import sys
from multiprocessing.managers import Value

class Card:
    suit_list = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
    rank_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def get_suit(self):
        return self._suit

    def get_rank(self):
        return self._rank


    def __str__(self):
        return f"the {self._rank} of {self._suit}"


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
    except ValueError:
        print(f"Invalid Rank: {rank}")
    #print(my_card)


