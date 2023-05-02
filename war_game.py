import random

# Represent a deck of cards

class Deck:
    def __init__(self, splitted_deck=None):
        if splitted_deck is None:
            self.cards = list(range(2, 15)) * 2
        else:
            self.cards = splitted_deck

    def shuffle(self):
        random.shuffle(self.cards)

    def split_deck(self, n):
        return self.cards[: len(self.cards) // n], self.cards[len(self.cards) // n :]

    # Removing one top card from the deck

    def place_card(self):
        return self.cards.pop(0)
    
    def take(self,cards_on_table):
        self.cards.extend(cards_on_table)
        
    def size(self):
        return len(self.cards)


def main():
    full_deck = Deck()
    full_deck.shuffle()
    # later move to function to make main less crowded
    deck1, deck2 = full_deck.split_deck(2)
    player1_deck = Deck(deck1)
    player2_deck = Deck(deck2)
    # Reveal opened cars for the players and state who takes the cards

    cards_on_table = []
    are_we_playing = True
    counter = 0
    while are_we_playing == True:
        while True:
            if player1_deck.size() == 0 or player2_deck.size() == 0:
                are_we_playing = False
                break

            counter += 1
            card1 = player1_deck.place_card()
            card2 = player2_deck.place_card()

            cards_on_table.append(card1)
            cards_on_table.append(card2)

            print(f"{counter}: Player 1: {card1}\tPlayer 2: {card2}\t{player1_deck.size()}:{player2_deck.size()}")

        #    print(f"Player 1: {show_opened_card(card1)}")
        #    print(f"Player 2: {show_opened_card(card2)}")
            # Compare values of opened cards and add cards to that player's deck, who won the round (had higher value card)

            if card1 > card2:
        #        print("Player 1 wins the round and takes the cards!")
                player1_deck.take(cards_on_table)
                cards_on_table = []
            elif card1 < card2:
                # print("Player 2 wins the round and takes the cards!")
                player2_deck.take(cards_on_table)
                cards_on_table = []
            else:
                if player1_deck.size() == 5 or player2_deck.size() == 5:
                    are_we_playing = False
                    break
                card1 = player1_deck.place_card()
                card2 = player2_deck.place_card()
                cards_on_table.append(card1)
                cards_on_table.append(card2)
                card1 = player1_deck.place_card()
                card2 = player2_deck.place_card()
                cards_on_table.append(card1)
                cards_on_table.append(card2)
                card1 = player1_deck.place_card()
                card2 = player2_deck.place_card()
                cards_on_table.append(card1)
                cards_on_table.append(card2)
                card1 = player1_deck.place_card()
                card2 = player2_deck.place_card()
                cards_on_table.append(card1)
                cards_on_table.append(card2)
                card1 = player1_deck.place_card()
                card2 = player2_deck.place_card()
                cards_on_table.append(card1)
                cards_on_table.append(card2)

    
    end_game (player1_deck.size,player2_deck.size)

    
def end_game(player1_number_of_cards,player2_number_of_cards):
    if player1_number_of_cards > player2_number_of_cards:
        print("The winner is player 1.")
    elif player1_number_of_cards < player2_number_of_cards:
        print("The winner is player 2.")
    else:
        print("It's a draw this time.")
    print("Thanks for playing!")
    

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
