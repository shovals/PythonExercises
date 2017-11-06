myList = []
SumTotal = 0
MultiplyTotal = 1

Input = raw_input('Enter a list of integers to draw from:')
InputClean = Input.split()

for item in InputClean:
    myList.append(item)

for number in myList:
    SumTotal += int(number)
    MultiplyTotal *= int(number)

print 'Sum is: ', SumTotal
print 'Multiply is:', MultiplyTotal
