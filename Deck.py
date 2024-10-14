from Card import Card
import random

class Deck:
    def __init__(self):
        self.cardlist = []
        for i in range(4):
            for j in range(13):
                self.cardlist.append(Card(j + 1, i + 1))

    def shuffle(self):
        random.shuffle(self.cardlist)

    def length(self):
        return len(self.cardlist)

    def deal_top_card(self):
        """ Remove and return the top card in the deck. """
        return self.cardlist.pop()

    def __str__(self):
        outstr = ''
        for card in self.cardlist:
            outstr = outstr + card.__str__() + '-'
        return outstr

deck = Deck()
#print(deck.length())