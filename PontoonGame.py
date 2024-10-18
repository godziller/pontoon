from Deck import Deck
from Dealer import Dealer
from Player import Player
import os
import platform


class PontoonGame(object):

    def __init__(self):
        self._pontoon = "PONTOON"
        self._deck = Deck()     #pontoon HAS A deck class#
        self._players = []      #this will hold the players for the game#
        self._dealer = Dealer()     #Instantiating the dealer for the game#



    def add_players(self, new_player):
        self._players.append(new_player)


    @property
    def players(self):
        return self._players

    @property
    def deck(self):
        return self._deck

    @property
    def dealer(self):
        return self._dealer

class Terminal(object):
    def __init__(self):
        self._name = "Terminal"

    def get_player_count(self):
        return input("How many players at the table?: ")

    def hit_or_stick(self, player):
        return input(f"{str(player)}:  Would you like to HIT (H) or STICK (S):  ").upper()

    def print_screen(self, player_list):
        os.system("clear")  #pretty printing by clearing the terminal each time before display table.
        print( f"{"Player":<10} | {"Hand":<30} | Count")
        print("-"*60)
        for player in player_list:
            print( f"{str(player):<10} | {str(player.hand):<30} | Count: {str(player.hand.value)}")
        print("-" * 60)

if __name__ == "__main__":
    my_game = PontoonGame()
    terminal = Terminal()
    player_count = terminal.get_player_count()      #how many playing game call#
    for number in range(int(player_count)):
        player = Player(f"Player_{number}")
        my_game.add_players(player)                 #adding player to the game

    my_game.deck.shuffle()

    #   ------START OF SETUP PHASE OF THE GAME------
    #we need to give every player 2 cards to begin with from the deck.
    for player in my_game.players:

        card1 = my_game.deck.deal_card()
        player.hand.add_card(card1)
        card2 = my_game.deck.deal_card()
        player.hand.add_card(card2)

    dealer_card1 = my_game.deck.deal_card()
    my_game.dealer.hand.add_card(dealer_card1)
    dealer_card2 = my_game.deck.deal_card()
    my_game.dealer.hand.add_card(dealer_card2)
    #   ------END OF SETUP PHASE OF THE GAME------


    for player in my_game.players:
        terminal.print_screen(my_game.players)
        play = terminal.hit_or_stick(player)
        print(play)
        while play == "H":
            hit_card = my_game.deck.deal_card()
            player.hand.add_card(hit_card)
            if (player.hand.value > 21):
                print(player.hand.value)
                print(f'Player {player} is bust with a hand of {player.hand.value}')
                break
            else:
                terminal.print_screen(my_game.players)
                play = terminal.hit_or_stick(player)
