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
             'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# Faced card dictionary and value of the number of turns for each face
face_card_num = {'Ace': 4, 'King': 3, 'Queen': 2, 'Jack': 1}
