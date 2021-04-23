# War - card game
# ----
# 2 player game – each player in alternate turn presses the ENTER key
# to flip a card from their deck and place in the middle deck.
#
# Options: --help AND --resume
# While playing player can type ‘--help’ to get game rules and ‘--resume’ to resume the game
# author: Jean-Marie Abel

import random

import os
import sys

from game_rules import game_rules


# function to clear screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


<<<<<<< HEAD
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
=======
# Player class
class Player():
    def __init__(self, player_id=0, name="", playerDeck=[]):
        self.player_id = player_id
        self.name = name
        self.player_deck = playerDeck
>>>>>>> 371d99a0e5b8a8a0328eff1fc0e461f97ccaba5e

    def getPlayerName(self):
        return self.name

    def getPlayerDeck(self):
        return self.player_deck

    def appendToPlayerDeck(self, middle_pile):
        for i in middle_pile:
            self.player_deck.insert(0, i)

    def popCardFromPlayerDeck(self):
        return self.player_deck.pop()

    def lengthPlayerDeck(self):
        return len(self.getPlayerDeck())

    def shafflePlayerPile(self):
        random.shuffle(self.getPlayerDeck())


# Playing piles class
class PlayingPiles():
    __face_cards = {'Ace': 14, 'King': 13, 'Queen': 12, 'Jack': 11}

    def __init__(self):
        self._middle_pile = []
        self._war_pile = []

    def appendToMiddlePile(self, card):
        self._middle_pile.append(card)

    def resetMiddlePile(self):
        self._middle_pile = []

    def appendToWarPile(self, card):
        self._war_pile.append(card)

    def getMiddlePile(self):
        return self._middle_pile

    def getWarPile(self):
        return self._war_pile

    def getFaceCard(self):
        return self.__face_cards

    def checkIfFaceCard(self, card):
        if card in self.__face_cards:
            return True
        return False

    def getFaceCardValue(self, card):
        if card in self.__face_cards:
            return self.__face_cards[card]
        return False

    def shaffleMiddlePile(self):
        random.shuffle(self.getMiddlePile())


def goingToWar():
    print("\033[0;31;47m\\n################ WAR STARTED ################\n")
    # append to war pile
    while True:
        still_has_cards = True
        # Starting war by adding 3 cards from each player to the middle pile
        for i in range(3):
            if len(playerOne.getPlayerDeck()) >= 3:
                playing_piles.appendToMiddlePile(
                    playerOne.popCardFromPlayerDeck())  # Get card from player 1 and add to war pile
            else:
                # Adding remaining cards to winning player deck
                for x in range(len(playerOne.getPlayerDeck())):
                    playerTwo.appendToPlayerDeck(playerOne.popCardFromPlayerDeck())
                still_has_cards = False

            if len(playerTwo.getPlayerDeck()) >= 3:
                playing_piles.appendToMiddlePile(
                    playerTwo.popCardFromPlayerDeck())  # Get card from player 2 and add to war pile
            else:
                # Adding remaining cards to winning player deck
                for x in range(len(playerTwo.getPlayerDeck())):
                    playerOne.appendToPlayerDeck(playerTwo.popCardFromPlayerDeck())
                still_has_cards = False

        if still_has_cards:
            card1, card2, card_1, card_2 = playerWarInputFunction()

            if int(card1) == int(card2):
                print(
                    f"\033[1;37;40m[WAR] {playerOne.getPlayerName()} AND {playerTwo.getPlayerName()} Have the same cards")
                goingToWar()
            elif int(card1) > int(card2):
                print(f"\033[1;37;40m[WAR] {playerOne.getPlayerName()} card {card1} is bigger then {card2}")
                playing_piles.shaffleMiddlePile()
                playerOne.appendToPlayerDeck(playing_piles.getMiddlePile())
                playerOne.shafflePlayerPile()
                playing_piles.resetMiddlePile()
                break
            else:
                print(f"[WAR] {playerTwo.getPlayerName()} card {card2} is bigger then {card1}")
                playing_piles.shaffleMiddlePile()
                playerTwo.appendToPlayerDeck(playing_piles.getMiddlePile())
                playerTwo.shafflePlayerPile()
                playing_piles.resetMiddlePile()
                break
        else:
            return still_has_cards

    print(
        f"\033[1;37;40m[WAR] Total cards in {playerOne.getPlayerName()} Deck {len(playerOne.getPlayerDeck())} ----- [{card_1} ==== {card_2}] ----- Total cards in {playerTwo.getPlayerName()} Deck {len(playerTwo.getPlayerDeck())}")
    print("\033[0;31;47m\n################ WAR ENDED ################\n")  # color red
    return card1, card2, card_1, card_2


# check user input
def checkInput(uInput):
    if uInput == "" or uInput == "--resume":
        return
    elif uInput == "--help":
        cls()
        game_rules(uInput)

    cls()
    return


# Regular player input
def playerInputFunction():
    # Get player One input

    uInput = input(f"\033[1;37;40m{playerOne.getPlayerName()} press ENTER key to flip a card: ")
    checkInput(uInput)  # Check user input
    card1 = playerOne.popCardFromPlayerDeck()  # Pop card form player 1 deck
    print(f"\033[1;33;40m{playerOne.getPlayerName()} just flipped card [{card1}]")
    card_1 = card1
    playing_piles.appendToMiddlePile(card1)  # Append popped card to middle deck

    # Get player Two input
    uInput = input(f"\033[1;37;40m{playerTwo.getPlayerName()} press ENTER key to flip a card: ")
    checkInput(uInput)  # Check user input
    card2 = playerTwo.popCardFromPlayerDeck()  # Pop card form player 2 deck
    print(f"\033[1;33;40m{playerTwo.getPlayerName()} just flipped card [{card2}]")
    card_2 = card2
    playing_piles.appendToMiddlePile(card2)  # Append popped card to middle deck

    # Check if popped card is a face card then get face card point value
    if playing_piles.checkIfFaceCard(card1):
        card1 = playing_piles.getFaceCardValue(card1)

    # Check if popped card is a face card then get face card point value
    if playing_piles.checkIfFaceCard(card2):
        card2 = playing_piles.getFaceCardValue(card2)

    return card1, card2, card_1, card_2


# War player input (War input happens when both players flipped the same cards)
def playerWarInputFunction():
    # Get player One input
    uInput = input(f"\033[1;37;40m[WAR] {playerOne.getPlayerName()} press ENTER key to flip a card: ")
    checkInput(uInput)  # Check user input
    card1 = playerOne.popCardFromPlayerDeck()  # Pop card form player 1 deck
    print(f"\033[1;33;40m[WAR] {playerOne.getPlayerName()} just flipped card [{card1}]")
    card_1 = card1
    playing_piles.appendToMiddlePile(card1)  # Append popped card to middle deck

    # Get player Two input
    uInput = input(f"\033[1;37;40m[WAR] {playerTwo.getPlayerName()} press ENTER key to flip a card: ")
    checkInput(uInput)  # Check user input
    card2 = playerTwo.popCardFromPlayerDeck()  # Pop card form player 2 deck
    print(f"\033[1;33;40m[WAR] {playerTwo.getPlayerName()} just flipped card [{card2}]")
    card_2 = card2
    playing_piles.appendToMiddlePile(card2)  # Append popped card to middle deck

    # Check if popped card is a face card then get face card point value
    if playing_piles.checkIfFaceCard(card1):
        card1 = playing_piles.getFaceCardValue(card1)
    # Check if popped card is a face card then get face card point value
    if playing_piles.checkIfFaceCard(card2):
        card2 = playing_piles.getFaceCardValue(card2)

    return card1, card2, card_1, card_2


# starting game

cls()
print("\033[1;32;40m=============================================")
print("\033[1;32;40m#         Playing War card game             #")
print("\033[1;32;40m=============================================")


def startGame():
    global winner
    global playerOneName
    global playerTwoName
    global playerOne
    global playerTwo
    global playing_piles

    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
            'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    player1_deck = []
    player2_deck = []

    random.shuffle(deck)

    switch_player = True

    for c in range(len(deck)):
        if switch_player:
            player1_deck.append(deck.pop())
            switch_player = False
        else:
            player2_deck.append(deck.pop())
            switch_player = True

    # return player1_deck, player2_deck

    # player1_deck, player2_deck = startGame()

    cls()
    print("\033[1;32;40m=============================================")
    print("\033[1;32;40m#         Playing War card game             #")
    print("\033[1;32;40m=============================================")

    playerOneName = input("\033[1;37;40mEnter Player One name: ")
    playerTwoName = input("\033[1;37;40mEnter Player Two name: ")

    playerOne = Player(1, playerOneName, player1_deck)
    playerTwo = Player(2, playerTwoName, player2_deck)

    playing_piles = PlayingPiles()

    while True:

        # Call input function
        card1, card2, card_1, card_2 = playerInputFunction()

        print("")
        print("")
        input(" --------- Press ENTER key to continue --------- ")
        print("")
        cls()
        print("\033[1;32;40m=============================================")
        print("\033[1;32;40m#         Playing War card game             #")
        print("\033[1;32;40m=============================================")

        if len(playerOne.getPlayerDeck()) <= 0 or len(playerTwo.getPlayerDeck()) <= 0:
            break
        else:
            print(
                f"\033[0;37;40m Total cards in {playerOne.getPlayerName()} Deck {len(playerOne.getPlayerDeck())} ----- [{card_1} ==== {card_2}] ----- Total cards in {playerTwo.getPlayerName()} Deck {len(playerTwo.getPlayerDeck())}")

        if int(card1) == int(card2):
            print(
                f"\033[0;37;40m **** {playerOne.getPlayerName()} AND {playerTwo.getPlayerName()} flipped the same cards ****")
            print("")
            if goingToWar() == False:
                break
            continue
        elif int(card1) > int(card2):
            print(f"\033[0;37;40m **** {playerOne.getPlayerName()} card [{card_1}] is bigger then card [{card_2}] ****")
            print("")
            playerOne.appendToPlayerDeck(playing_piles.getMiddlePile())
            playing_piles.resetMiddlePile()
        else:
            print(f"\033[0;37;40m **** {playerTwo.getPlayerName()} card [{card_2}] is bigger then card [{card_1}] ****")
            print("")
            playerTwo.appendToPlayerDeck(playing_piles.getMiddlePile())
            playing_piles.resetMiddlePile()

        if len(playerOne.getPlayerDeck()) < 1:
            break

        if len(playerTwo.getPlayerDeck()) < 1:
            break

    if len(playerOne.getPlayerDeck()) <= 1:
        print(f"\033[1;32;40m--------------------WINNER-------------------------")
        print("")
        print(f"\033[1;32;40m*** {playerTwo.getPlayerName().upper()} is the WINNER ***")
        print("")
        answer = input("\033[1;37;40mWould you like to play War again [Y]es / [N]o : ").lower()
        if answer == 'y' or answer == 'yes':
            startGame()
        else:
            sys.exit()

    if len(playerTwo.getPlayerDeck()) <= 1:
        print(f"\033[1;32;40m--------------------WINNER-------------------------")
        print("")
        print(f"\033[1;32;40m*** {playerOne.getPlayerName().upper()} is the WINNER ***")
        print("")
        answer = input("\033[1;37;40mWould you like to play War again [Y]es / [N]o : ").lower()
        if answer == 'y' or answer == 'yes':
            startGame()
        else:
            sys.exit()


answer = input("\033[1;37;40mWould you like to play War [Y]es / [N]o : ").lower()
if answer == 'y' or answer == 'yes':
    startGame()