def CheckIt(letter):
    Vowel = ['a','e','i','o','u']
    if letter in Vowel:
        return True
    else:
        return False


User = raw_input('Enter a letter: ')
if CheckIt(User) == True:
    print 'It is a vowel'
else:
    print 'It is not a vowel'

