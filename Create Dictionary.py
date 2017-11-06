# reads a txt file which is colon separated and extract the username (first place) and the ID (third place)
# ignores commented lines

filename = raw_input('Enter the file name: ')
f = open(filename, "r")

for line in f:
    currentline = line.split(':')
    if not (currentline[0].startswith('#')):
        print currentline[0], currentline[2]
