# this script gets a list of integers and draw a histogram accordingly

import array

def Histogram(astrix):
    print '*' * astrix

myList = []
Draw = raw_input('Enter a list of integers to draw from:')
DrawClean = Draw.split()

for item in DrawClean:
    myList.append(item)

for number in myList:
    Histogram(int(number))



