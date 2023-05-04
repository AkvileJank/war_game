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

    def take(self, cards_on_table):
        self.cards.extend(cards_on_table)

    def size(self):
        return len(self.cards)


def main():
    show_game_rules()
    player1_name, player2_name = set_player_name()
    full_deck = Deck()
    full_deck.shuffle()
    deck1, deck2 = full_deck.split_deck(2)
    player1_deck = Deck(deck1)
    player2_deck = Deck(deck2)

    cards_on_table = []
    are_we_playing = True
    # counter = 0
    while are_we_playing == True:
        show_card_amount(player1_name, player1_deck, player2_name, player2_deck)
        while True:
            if player1_deck.size() == 0 or player2_deck.size() == 0:
                are_we_playing = False
                break
            # print(player1_deck.size(), " ", player2_deck.size())
            # counter += 1
            card1, card2 = place_both_cards(player1_deck, player2_deck)
            print_both_cards(player1_name, player2_name, card1, card2)
            add_cards_to_table(cards_on_table, card1, card2)

            # Compare values of opened cards and add cards to that player's deck, who won the round (had higher value card)

            if card1 > card2:
                print(f"{player1_name} wins the round and takes the cards!")
                player1_deck.take(cards_on_table)
                show_card_amount(player1_name, player1_deck, player2_name, player2_deck)
                cards_on_table = []
            elif card1 < card2:
                print(f"{player2_name} wins the round and takes the cards!")
                player2_deck.take(cards_on_table)
                show_card_amount(player1_name, player1_deck, player2_name, player2_deck)
                cards_on_table = []
            else:
                if player1_deck.size() == 4 or player2_deck.size() == 4:
                    are_we_playing = False
                    break
                i = 0
                while i < 3:
                    try:
                        card1, card2 = place_both_cards(player1_deck, player2_deck)
                        add_cards_to_table(cards_on_table, card1, card2)
                        i += 1
                    except IndexError:
                        print("Not enough cards are left to continue playing!")
                        are_we_playing = False
                        break

    end_game(player1_name, player2_name, player1_deck.size(), player2_deck.size())


def show_game_rules():
    print('Welcome to card game "War"!')
    game_rules = (
        "Shuffled deck of cards is splitted equaly for 2 players. "
        "The top card from player's decks is revealed at each round "
        "and the player with higher card wins the round and takes revealed cards. "
        "If there is a tie, each player places three cards face down and one card "
        "face up, and the higher face-up card wins all the placed cards. "
        "The game can continue until player has all the cards/has no cards left."
    )

    print(game_rules)
    print("Good luck!")


def set_player_name():
    player1_name = input("Enter player 1 name: ")
    player2_name = input("Enter player 2 name: ")
    return player1_name, player2_name


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


def print_both_cards(player1_name, player2_name, card1, card2):
    print(f"{player1_name}: {show_opened_card(card1)}")
    print(f"{player2_name}: {show_opened_card(card2)}")


def place_both_cards(player1_deck, player2_deck):
    card1 = player1_deck.place_card()
    card2 = player2_deck.place_card()
    return card1, card2


def add_cards_to_table(cards_on_table, card1, card2):
    cards_on_table.extend([card1, card2])


def end_game(player1, player2, player1_number_of_cards, player2_number_of_cards):
    if player1_number_of_cards > player2_number_of_cards:
        print(f"The winner is {player1}.")
    elif player1_number_of_cards < player2_number_of_cards:
        print(f"The winner is {player2}.")
    else:
        print("It's a draw this time.")
    print("Thanks for playing!")


def show_card_amount(player1_name, player1_deck, player2_name, player2_deck):
    print(f"{player1_name} has {player1_deck.size()} cards")
    print(f"{player2_name} has {player2_deck.size()} cards")


if __name__ == "__main__":
    main()
