import random
letters = []
hangmanOutput = []
count = 0
first = True

with open('sowpods.txt') as f:
    words = list(f)
selectedWord = random.choice(words)
# print selectedWord

for letter in selectedWord:
    if letter == "\n":
        pass
    else:
        letters.append(letter)

# print "".join(letters)

print ">>> Welcome to Hangman!\n"

while letters != hangmanOutput:
    userGuess = raw_input(">>> Guess your letter:")
    for guess in letters:
        if guess == userGuess:
            if first:
                hangmanOutput.insert(count, guess)
                count += 1
            else:
                hangmanOutput[count] = guess
                count += 1
        else:
            if first:
                hangmanOutput.insert(count, "_")
                count += 1
            else:
                count += 1
    first = False
    print "".join(hangmanOutput)
    count = 0

print "You guessed it! " \
      "The word is: {}".format("".join(hangmanOutput))



