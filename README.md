# war_game

Game rules: 

Shuffled deck of cards is splitted equaly for 2 players. The top card from player's decks is revealed at each round and the player with higher card wins the round and takes revealed cards. If there is a tie, each player places three cards face down and one card face up, and the higher face-up card wins all the placed cards. The game can continue until player has all the cards/has no cards left.

For this task I chose to implement game logic with 2 players, who play against each other, face - up cards are showed, face-down cards are just counted but not printed to not reveal them.

Task requirements:

Represent the deck of cards in your program (use a list or a tuple of strings or integers representing each card)

Assign numeric values in code to non - numeric cards (jack, king, queen, ace)

Create a function to shuffle the deck of cards (can use the shuffle function from the random module in Python)

Create a function to deal the cards to the two players (can use slicing to split the deck of cards in half)

Create a function to compare the cards that the two players have played

!Create a function to handle the case where there is a tie. In this case, the players play another round and add the new cards to the ones they have already played.

!Create a function to update amount of cards the two players have after each round.

!Create a function to check if the game is over. The game is over when player has no cards left, the other player is winner

!Create a function to play the game. This function will call the other functions in the correct order and keep track of the game state.

!Add necessary user interface or input/output functionality to your program:

	*Display the game's rules at the beginning of the game (plus total amount of cards in 	deck)

	*Prompt the user to enter their name or choose a player name at the beginning of the game.

	Display the cards that each player plays during a round of the game.
	
	*Display the score of each player after each round of the game (amount of cards in their decks).

	*Prompt the user to play another round or end the game after each round.

	*Display a message when the game is over and declare the winner.