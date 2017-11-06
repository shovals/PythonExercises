import random
from playsound import playsound


def dice_print(number):
    if number == 1:
        print "---------"
        print "|       |"
        print "|   X   |"
        print "|       |"
        print "---------"
    if number == 2:
        print "---------"
        print "| X     |"
        print "|       |"
        print "|     X |"
        print "---------"
    if number == 3:
        print "---------"
        print "|  X    |"
        print "|   X   |"
        print "|    X  |"
        print "---------"
    if number == 4:
        print "---------"
        print "| X   X |"
        print "|       |"
        print "| X   X |"
        print "---------"
    if number == 5:
        print "---------"
        print "| X   X |"
        print "|   X   |"
        print "| X   X |"
        print "---------"
    if number == 6:
        print "---------"
        print "| X   X |"
        print "| X   X |"
        print "| X   X |"
        print "---------"


if __name__ == '__main__':
    RollAgain = True
    while RollAgain:
        playsound("rolling-dice.wav")
        DiceOne = random.randrange(1, 6, 1)
        dice_print(DiceOne)
        DiceTwo = random.randrange(1, 6, 1)
        dice_print(DiceTwo)
        user = raw_input("Do you want to roll again? (Y/N)")
        if user == "Y" or user == "y":
            RollAgain = True
        else:
            RollAgain = False





