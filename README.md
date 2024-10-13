# pontoon
Second Year Python OOP Project 

Enter some text to describe the Python game.

## Design
Classes: 

* Card
* Hand
* Deck
* PontoonCard
* Player
* House
* PontoonGame

```mermaid

classDiagram
    Card <|-- PontoonCard

    class Card{
        -string suit
        -string rank
        -int value
    }
    class PontoonCard{
        +get_value()
    }

```