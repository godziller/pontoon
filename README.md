# pontoon
Second Year Python OOP Project 

Enter some text to describe the Pontoon game.

## Design
Classes: 

* Card: Simple Card Class. Expected to be inherited with game specific value
* PontoonCard: subclass of Card. Sets face cards to 10 and Ace to 11
* Hand: Represents a players hand. A collection of Cards and a hand value
* Deck: Collection of cards to begin. Expect to pop cards as dealt and move cards onto Hand array
* Player: Represents a player
* House: Special Player - no interaction, a play() will finish out game
* PontoonGame: Need a class for pulling everything together and contorlling the game logic

```mermaid

classDiagram
    Card <|-- PontoonCard
    Deck --> PontoonCard: array of
    Hand --> PontoonCard: array of
    Person --> Hand: has a
    House --|> Person
    note for Card "we don't store value 'cos different games
        may have different card values for same card.
        Pontoon King = 10, but Snap has no value"
        
    note for House "play_out is called when all Players finished,
    it should be fed the count to beat.
    With that it deals itself cards until its count >= the target
    or until it goes bust"    
    class Card{
        -string _suit
        -string _rank
        +get_suit()
        +get_rank()
    }
    class PontoonCard{
        -int _value

        +get_value()
    }
    class Deck{
    -PontoonCard _cards[]
    void shuffle_deck()
    PontoonCard deal_card()
    }
    class Hand{
        PontoonCard _cards[]
        add_card(Card)
        int count_hand()
    }
    class Person{
        -string __name
        -Hand hand
    }
    class House{
        int play_out(count_to_beat)
        
    }
    

```