# max of 3 show the largest number from 3 numbers

One = input('Enter first number: ')
Two = input('Enter second number: ')
Third = input('Enter third number: ')


if One > Third and One > Two:
    print 'Max is ', One
elif Two > One and Two > Third:
    print 'Max is ', Two
else:
    print 'Max is', Third