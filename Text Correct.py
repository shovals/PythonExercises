# This script get a string and perform the following corrections on it
# 1. Reduce 2 or more spaces into 1
# 2. Add space after a comma

UpdatedString =''
good = ''
String = raw_input('Enter a string to correct: ')
for char in String:
    if char == ',':
        UpdatedString = UpdatedString + char + ' '
    else:
        UpdatedString += char
for a in UpdatedString.split():
    good += a
    good += ' '

print good