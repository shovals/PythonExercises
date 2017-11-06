# script that checks if a string can be written straight or backwards and it stays the same, like RADAR

with open('list-to-check.txt', 'r') as f:
    for word in f:
        word = word.replace('\n', '')
        if word == word[::-1]:
            print word, 'is a palindrom !'
        else:
            print word, 'is not a palindrom'

