from random import randint

Name = raw_input('Enter your name: ')
RandNumber = randint(1,20)
Guess = int(raw_input('Guess a number between 1 and 20: '))
Success = False

while Success != True:
    if Guess > RandNumber:
        Guess = int(raw_input('Guess too high, try again: '))
    elif Guess < RandNumber:
        Guess = int(raw_input('Guess too short, try again: '))
    else:
        print 'You guessed right !'
        Success = True

