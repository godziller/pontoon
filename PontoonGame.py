from Deck import Deck
from Dealer import Dealer
from Player import Player
import os



class PontoonGame(object):

    def __init__(self):
        """
        PontoonGame represents an instance of a game of Pontoon.

        The PontoonGame card is reponsible for setting up the game. Thi
        This involves:
        Creating a deck
        Creating a dealer
        Adding players
        This class also holds a _game_leader reference to a player instance, which is the current game leader based on hand value
        """

        self._pontoon = "PONTOON"
        self._deck = Deck()     #pontoon HAS A deck class#
        self._players = []      #this will hold the players for the game#
        self._dealer = Dealer(self._deck)     #Instantiating the dealer for the game#
        self._game_leader = None              #Going to use this value to determine the game leader (player with greatest points)
        self._players.append(self._dealer)    #Adding the dealer to print everyone.

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
        """
        The Terminal Class encapsulates all interaction with the game prompt

        THe Terminal Class is responsible for:
        Getting the number of players wishing to play the game.
        Asking a player whether they want to hit or stick
        Printing the 'table' info to screen
        """

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

    def print_winner(self, player_list):
        winning_hand = 0
        winning_player = None
        for player in player_list:
            if player.hand.value > winning_hand:
                winning_hand = player.hand.value
                winning_player = player

        print(f"The winning player is!: {winning_player}")

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


    #   ------END OF SETUP PHASE OF THE GAME------

    # ----- Loop over every player playing and engage with each in turn
    for player in my_game.players:
        if not isinstance(player, Dealer): # ONLY want to loop here on players, not dealer obj.

            terminal.print_screen(my_game.players)
            play = terminal.hit_or_stick(player)
            print(play)
            while play == "H":

                #The logic of a player hitting is to remove a card object from
                #-the deck and add it to the players hand.
                hit_card = my_game.deck.deal_card()
                player.hand.add_card(hit_card)
                if (player.hand.value > 21):
                    print(player.hand.value)
                    player.hand.value = 0       #flattening the value when bust to 0.
                    break
                else:
                    terminal.print_screen(my_game.players)
                    play = terminal.hit_or_stick(player)
            # Record the highest count across all players and use that for the dealer

    # -------- Need to put the dealer in play now.
        count_to_beat = 0
                            #collect the value.#
    for player in my_game.players:
        if not isinstance(player, Dealer): # ONLY want to loop here on players, not dealer obj.
            if player.hand.value > count_to_beat:
                count_to_beat = player.hand.value
                my_game._game_leader = player

    if my_game.dealer.play_out(count_to_beat) > 21:
        my_game.dealer.hand.value = 0
    terminal.print_screen(my_game.players)
    terminal.print_winner(my_game.players)
