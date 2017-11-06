Count = 0
StringInput = raw_input('Please enter the string: ')
print 'Built in length show:', len(StringInput)
for letter in StringInput:
    Count = Count + 1

print 'Measured length:', Count
