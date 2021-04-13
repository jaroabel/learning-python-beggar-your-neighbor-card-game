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

        print(f"{display_cards[0]}")
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
        return False



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

    def getPlayerId(self):
        return self.player_id

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



# Function checking user input
def checkUserInput(uInput):
    if uInput == "--help" or uInput == "--resume":
        return display_rules(uInput)
    else:
        return True


def counterPlayerFaceCard(player_id, numVal):
    if player_id == 1:
        name = playerOne.getName()
    else:
        name = playerTwo.getName()

    print(f"A face card was flipped by {name} you have {numVal} chance(s) to counter with a face card of your own")
    for i in range(numVal):
        print(f"counter 'i' ==> {i} and var 'numVal' {numVal}")
        if player_id == 1:
            uInput = input("{} Press ENTER key to play a card: ".format(playerTwo.getName())).lower()
            if uInput != "": # and checkUserInput(uInput) == False:
                uInput = input("{} Press ENTER key to play a card: ".format(playerTwo.getName())).lower()

            elif uInput == "":
                popedCard = playerTwo.getAcardFromPlayerDeck()  # Flip card from players deck
                print(f"Poped card {popedCard}")
                game_process.addToDiscardDeck(popedCard)  # Add card to discard deck
                isFace, numVal = game_process.checkIfFaceCard(popedCard)  # Check if flipped card is a face card
                if isFace:
                    counterPlayerFaceCard(2, numVal)
                else:
                    print(displayPlayingTable(popedCard))
                    continue
        if player_id == 2:
            print(f"counter 'i' ==> {i} and var 'numVal' {numVal}")
            uInput = input("{} Press ENTER key to play a card: ".format(playerOne.getName())).lower()
            if uInput != "": # and checkUserInput(uInput) == False:
                uInput = input("{} Press ENTER key to play a card: ".format(playerOne.getName())).lower()

            elif uInput == "":
                popedCard = playerOne.getAcardFromPlayerDeck()  # Flip card from players deck
                game_process.addToDiscardDeck(popedCard)  # Add card to discard deck
                isFace, numVal = game_process.checkIfFaceCard(popedCard)  # Check if flipped card is a face card
                if isFace:
                    counterPlayerFaceCard(1, numVal)
                else:
                    print(displayPlayingTable(popedCard))
                    continue


        return player_id



# Initializing Player and GameProcess class
playerOne = Player(players_id[0])
playerTwo = Player(players_id[1])
game_process = GameProcess()

def displayPlayingTable(playedCard):
    return display_cards[0].format(len(playerOne.getPlayerDeck())) + " " + display_cards[1].format(playedCard) + " " + display_cards[0].format(len(playerTwo.getPlayerDeck()))



#  Initializing game
player_deck_assigned = game_setting(player_deck_assigned)

print(f"Player 1 ==> {playerOne}")
print(f"Player 1 ==> {playerTwo}")

playing_turns  = 1 #
#cls()

def playGame(playingTurns):
    while True:
         print(f"Current player ===> {playingTurns}")
         if playingTurns == 1:
            uInput = input("{} Press ENTER key to play a card: ".format(playerOne.getName())).lower()
            if uInput != "" and not checkUserInput(uInput):
                uInput = input("{} Press ENTER key to play a card: ".format(playerOne.getName())).lower()
                # check if only ENTER key was pressed
            elif uInput == "":
                popedCard = playerOne.getAcardFromPlayerDeck() # Flip card from players deck
                print(f"Popped card ==> {popedCard}")
                game_process.addToDiscardDeck(popedCard) # Add card to discard deck
                isFace, numVal = game_process.checkIfFaceCard(popedCard) # Check if flipped card is a face card
                if isFace:
                    print(displayPlayingTable(popedCard))
                    player_id = counterPlayerFaceCard(1, numVal)
                    if player_id == 1:
                        playerOne.addToPlayerDeck(game_process.getDiscardDeck())
                    else:
                        playerTwo.addToPlayerDeck(game_process.getDiscardDeck())

                    game_process.resetDiscardDeck()
                else:
                    print(displayPlayingTable(popedCard))
                    playingTurns = 2
            else:
                print("Error: {}, You Please press the ENTER Key, or type '--help' or '--resume' ")
                playGame(1)
            playingTurns = 2
         elif playingTurns == 2:
             uInput = input("{} Press ENTER key to play a card: ".format(playerTwo.getName())).lower()
             if uInput != "" and not checkUserInput(uInput):
                 uInput = input("{} Press ENTER key to play a card: ".format(playerTwo.getName())).lower()
             # check if only ENTER key was pressed
             elif uInput == "":
                 popedCard = playerTwo.getAcardFromPlayerDeck()  # Flip card from players deck
                 game_process.addToDiscardDeck(popedCard)  # Add card to discard deck
                 isFace, numVal = game_process.checkIfFaceCard(popedCard)  # Check if flipped card is a face card
                 if isFace:
                     print(displayPlayingTable(popedCard))
                     player_id = counterPlayerFaceCard(1, numVal)
                     if player_id == 1:
                         playerOne.addToPlayerDeck(game_process.getDiscardDeck())
                     else:
                         playerTwo.addToPlayerDeck(game_process.getDiscardDeck())
                     game_process.resetDiscardDeck()
                 else:
                     print(displayPlayingTable(popedCard))
                     playingTurns = 1
             else:
                 print("Error: {}, You Please press the ENTER Key, or type '--help' or '--resume' ")
                 playGame(2)
             playingTurns = 1


displayTable = display_cards[0].format(len(playerOne.getPlayerDeck())) + " " + display_cards[2] + " " + display_cards[0].format(len(playerTwo.getPlayerDeck()))
print(displayTable)
playGame(playing_turns)



