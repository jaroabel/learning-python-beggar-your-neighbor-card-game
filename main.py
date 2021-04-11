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

