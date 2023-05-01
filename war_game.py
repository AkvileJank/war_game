import random

# Represent a deck of cards

class Deck:
    def __init__(self, splitted_deck=None):
        if splitted_deck is None:
            self.cards = list(range(2, 15)) * 4
        else:
            self.cards = splitted_deck

    def shuffle(self):
        random.shuffle(self.cards)

    def split_deck(self, n):
        return self.cards[: len(self.cards) // n], self.cards[len(self.cards) // n :]

    # Removing one top card from the deck

    def place_card(self):
        return self.cards.pop(0)


def main():
    full_deck = Deck()
    full_deck.shuffle()
    # later move to function to make main less crowded
    deck1, deck2 = full_deck.split_deck(2)
    player1_deck = Deck(deck1)
    player2_deck = Deck(deck2)

    # Reveal opened cars for the players and state who takes the cards
    card1 = player1_deck.place_card()
    card2 = player2_deck.place_card()

    print(f"Player 1: {show_opened_card(card1)}")
    print(f"Player 2: {show_opened_card(card2)}")

    # Compare values of opened cards and add cards to that player's deck, who won the round (had higher value card)

    if card1 > card2:
        print("Player 1 wins the round and takes the cards!")
        player1_deck.cards.extend([card1, card2])
    elif card1 < card2:
        print("Player 2 wins the round and takes the cards!")
        player2_deck.cards.extend([card1, card2])


# Print J, Q, K, A to user instead of numeric values

def show_opened_card(card):
    match card:
        case 11:
            return "J"
        case 12:
            return "Q"
        case 13:
            return "K"
        case 14:
            return "A"
        case _:
            return card


if __name__ == "__main__":
    main()
