# War - card game
# ----
# Displays War game rules
# Options: --help AND --resume
# While playing player can type ‘--help’ to get game rules and ‘--resume’ to resume the game
# author: Jean-Marie Abel

def game_rules(uInput):
    if uInput == "--help":
        print(
            "\033[0;31;47m============================================================================================================================")
        print("""\033[1;33;40m
        The goal is to be the first player to win all 52 cards\n\n

        --THE DEAL--\n
        The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down.\n
        Anyone may deal first. Each player places their stack of cards face down, in front of them.\n\n

        --THE PLAY--\n
        If the two cards played are of equal value, then there is a "war". Both players place the next three cards face down\n
        and then another card face-up. The owner of the higher face-up card wins the war and adds all the cards on the table\n
        to the bottom of their deck. If the face-up cards are again equal then the battle repeats with another set of face-down/up\n
        cards. This repeats until one player's face-up card is higher than their opponent's.\n\n

        --HOW TO KEEP SCORE--\n
        The game ends when one player has won all the cards.\n
        """)
        print(
            "\033[0;31;47m============================================================================================================================")
        uInput = input("\033[1;37;40mEnter '--resume' to return to the game: ").lower()
        if uInput == "--resume" or uInput == "--help":
            game_rules(uInput)
        else:
            return

    elif uInput == "--resume":
        return
    else:
        return