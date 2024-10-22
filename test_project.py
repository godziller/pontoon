# Student Number: 123411792
from Card import Card
from Dealer import Dealer
from PontoonCard import PontoonCard
from Deck import Deck
from Hand import Hand
from Player import Player

# Test Card class
def test_Card():
    suit = 'Spades'
    junk = 'Junk'
    rank = "K"

    try:
        my_card = Card(suit, rank)
    except:
        print(f"Invalid Suit: {suit}")

    try:
        my_card = Card(junk, rank)
    except:
        print(f"Invalid Suit: {junk}")

def test_PontoonCard():
    suit = 'Spades'
    junk = 'Junk'
    rank =  "K"

    try:
        my_card = PontoonCard(suit, rank)
    except:
        print(f"Invalid Suit: {suit}")

    try:
        my_card = PontoonCard(junk, rank)
    except:
        print(f"Invalid Suit: {junk}")

def test_Deck():
    try:
        my_deck = Deck()
    except:
        print("Test Deck  creation failed")



def test_Deck_operations():
    try:
        my_deck = Deck()
        my_deck.shuffle()
        my_deck.length()
        my_deck.deal_card()
    except:
        print("Deck operations failed")

def test_Hand():
    my_hand = Hand()

def test_Hand_operations():
    my_hand = Hand()
    my_card = PontoonCard('Hearts', 'A')
    my_hand.add_card(my_card)

def test_Player():
    my_player = Player("Darren")

def test_Player_operations():
    my_player = Player("Darren")
    my_card = PontoonCard('Hearts', 'A')
    my_player.hand.add_card(my_card)
    my_player.hand.get_value()

def test_Dealer():
    my_deck = Deck()
    my_dealer = Dealer(my_deck)

def test_Dealer_operations():
    my_deck = Deck()
    my_dealer = Dealer(my_deck)
    my_dealer.play_out(21)

if __name__ == "__main__":
    test_Card()
    test_PontoonCard()
    test_Deck()
    test_Deck_operations()
    test_Hand()
    test_Hand_operations()
    test_Player()
    test_Player_operations()
    test_Dealer()
    test_Dealer_operations()

"""
Test Report
pytest test_project.py 
============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/ziller/Repos/pontoon
collected 10 items                                                             

test_project.py ..........                                               [100%]

============================== 10 passed in 0.01s ==============================

"""
