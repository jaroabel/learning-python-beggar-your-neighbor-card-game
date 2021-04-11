# Beggar My Neighbor - Card Game
#
# 2 player game – each player in alternate turn presses the ENTER key
# to flip a card from their deck and place in the middle deck.
#
# Options: --help AND --resume
# While playing player can type ‘--help’ to get game rules and ‘--resume’ to resume the game
# author: Jean-Marie Abel

import random
import os


# function to clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Playing card deck list
card_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
             'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4',
             '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9',
             '10', 'Jack', 'Queen', 'King']

display_cards = ["""
________
| TOTAL |
| CARDS |
|   {}  |
--------""", """
________
|      |
|  {}  
|      |
--------""", """
________
|      |
|      |
|      |
--------"""]
player_deck_assigned = False
players_id = (1, 2)



# Display rules function
def display_rules(uInput):
    cls()
    print(f"User choice: {uInput}")
    while True:
        rulesInput = input(f"Type --resume to resume game: ").lower()
        if rulesInput != "--help" and rulesInput != "--resume":
            print("[Error] please enter --help OR --resume: ")
        elif rulesInput == "--help":
            display_rules(rulesInput)
            break
        else:
            break

    if playerOne.getName() == "" and playerTwo.getName() == "":
        cls()
        print("In condition 1")
        game_setting(False)
    elif playerOne.getName() != "" or playerTwo.getName() != "":
        cls()
        print("In condition 2")
        game_setting(False)
    else:
        cls()
        return_to_currentGame()



# Function to initialize the game (get player name, shuffle and split deck)
def game_setting(playerDeckAssigned):
    # First initialization has to be done only once
    if not playerDeckAssigned:
        alternate_deck = True
        # Shuffle main card deck
        random.shuffle(card_deck)
        player1_deck = []
        player2_deck = []
        # Splitting the main deck between the two players
        for i in range(len(card_deck) - 1, -1, -1):
            if alternate_deck:
                # adding cards to player 1 deck
                player1_deck.append(card_deck[i])
                alternate_deck = False
            else:
                # adding cards to player 2 deck
                player2_deck.append(card_deck[i])
                alternate_deck = True

        # Setting players one
        if playerOne.getName() == "":
            userInput = input("Enter player 1 name: ").lower()
            if userInput == "--help" or userInput == "--resume":
                display_rules(userInput)
            else:
                playerOne.setName(userInput.capitalize())
                playerOne.setPlayerDeck(player1_deck)

        # Setting players two
        if playerTwo.getName() == "":
            userInput = input("Enter player 2 name: ").lower()
            if userInput == "--help" or userInput == "--resume":
                display_rules(userInput)
            else:
                playerTwo.setName(userInput.capitalize())
                playerTwo.setPlayerDeck(player2_deck)

    if playerOne.getName() != "" and playerTwo.getName() != "" and len(playerOne.getPlayerDeck()) > 0 and len(playerTwo.getPlayerDeck()) > 0:
        return True


# resume current playing game
def return_to_currentGame():
    print("Back to game")

# Player class
class Player():
    _player_name = ""
    _player_deck = []

    def __init__(self, player_id=""):
        self.player_id = player_id

    def setName(self, name):
        self._player_name = name

    def setPlayerDeck(self, playerDeck):
        self._player_deck = playerDeck

    def getName(self):
        return self._player_name

    def getPlayerDeck(self):
        return self._player_deck

    def getAcardFromPlayerDeck(self):
        return self._player_deck.pop()

    def addToPlayerDeck(self, discardCards):
        for i in discardCards:
            self._player_deck.append(i)

    def __str__(self):
        return "Player ID: " + str(self.player_id) + " --- Player name: " + self._player_name + " --- Player deck: " + str(self._player_deck)

# Class processing user flipped card, checking if card flipped a face card
class GameProcess():
    _face_cards = {'Ace': 4, 'King': 3, 'Queen': 2, 'Jack': 1} # Faced card dictionary and value of the number of turns for each face
    _discard_deck = [] # List that will contain all players flipped cards

    def addToDiscardDeck(self, cardPlayed):
        self._discard_deck.append(cardPlayed)

    def resetDiscardDeck(self):
        self._discard_deck = []

    def checkIfFaceCard(self, card):
        if card in self._face_cards:
            return True, self._face_cards[card]
        else:
            return False, None

    def getDiscardDeck(self):
        return self._discard_deck



# Initializing Player and GameProcess class
playerOne = Player(players_id[0])
playerTwo = Player(players_id[1])
game_process = GameProcess


#  Initializing game
player_deck_assigned = game_setting(player_deck_assigned)

print(f"Player 1 ==> {playerOne}")
print(f"Player 1 ==> {playerTwo}")

# playing_turns  = True # True = Player 1 start first turn
# cls()

# while True:
#     if playing_turns:
#         popedCard = playerOne.getAcardFromPlayerDeck() # Flip card from players deck
#         game_process.addToDiscardDeck(popedCard) # Add card to discard deck
#         isFace, numVal = game_process.checkIfFaceCard(popedCard) # Check if flipped card is a face card
#         if isFace:
#             print(f"A face card was flipped by {playerOne.getName()} you have {numVal} chance(s) to counter with a face card of your own")
#             for i in range(numVal):
#                 uInput = input("Press ENTER key to play a card: ")
#                 if uInput == ""
#                    popedCard = playerTwo.getAcardFromPlayerDeck()  # Flip card from players deck
#                     game_process.addToDiscardDeck(popedCard)  # Add card to discard deck
#                     isFace, numVal = game_process.checkIfFaceCard(popedCard)  # Check if flipped card is a face card
#                     if isFace:
#                         playerOne.addToPlayerDeck()


#                elif uInput == "--help" or uInput == "--resume":
#                     display_rules(uInput)



