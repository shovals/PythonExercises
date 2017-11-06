# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

symbols = '~`;:!@#$%^&*()_-+|"?/<>*.'


def a_to_z(password):
    small_letters, cap_letters = False, False

    for letter in password:
        if letter.islower():
            small_letters = True
    for letter in password:
        if letter.isupper():
            cap_letters = True

    if (small_letters == True) and (cap_letters == True):
        return True
    else:
        return False

def zero_to_nine(password):
    for letter in password:
        if letter.isdigit():
            return True
        else:
            return False

def special_char(password):
    symbol = False

    for letter in password:
        if letter in symbols:
            return True

    if symbol == False:
        return False


def length(password):
    if len(password) <= 16 and len(password) >= 6:
        return True
    else:
        return False


print """ 
Enter a password to check according to the following:
* At least 1 letter between [a-z] and 1 letter between [A-Z]
* At least 1 number between [0-9]
* At least 1 character from [$#@]
* Minimum length 6 characters
* Maximum length 16 characters      
"""
password = raw_input("Enter your password: ")
print "A to Z check: ", a_to_z(password)
print "0 to 9 check: ", zero_to_nine(password)
print "Special char check: ", special_char(password)
print "Length check: ", length(password)
print ""

if a_to_z(password) == True and zero_to_nine(password)==True and special_char(password)==True and length(password)==True:
    print "Password checks OK"
else:
    print "Password Not OK"