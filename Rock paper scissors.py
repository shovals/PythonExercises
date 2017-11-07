import random


def whowins(user, pc):
    # decide who wins based on the results
    if user == pc:
        print "Tie\n"
    elif user == 0 and pc == 2:
        print "You win!\n"
    elif user == 1 and pc == 0:
        print "You lose\n"
    elif user == 2 and pc == 1:
        print "You win!\n"


def rollconvert(draw):
    # convert the input number into the real text
    if draw == 0:
        return "Rock"
    elif draw == 1:
        return "Paper"
    elif draw == 2:
        return "Scissors"
    else:
        return "Not a valid option"

rollanother = True
options = [0, 1, 2]


print """
0 - Rock
1 - Paper
2 - Scissors
"""
while rollanother:
    userSelection = input("Enter your selection:")
    computerSelection = random.choice(options)
    print "You drew {}\nPC drew {}".format(rollconvert(userSelection), rollconvert(computerSelection))
    whowins(userSelection, computerSelection)

    continuePlay = raw_input("Roll another? Y/N")
    if continuePlay == "Y" or continuePlay == "y":
        rollanother = True
    elif continuePlay == "N" or "n":
        rollanother = False
