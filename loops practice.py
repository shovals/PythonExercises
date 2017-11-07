# print the even numbers from 2 to 100, inclusive
#for i in range(2, 102,2):
#    print i

# count down from 10 to 0 until blast off
# i = 10
# while i > -1:
#    print i
#    i = i - 1
# print "Blast off!!!"

# ask the user for 7 numbers
# print total sum of the numbers
# print count of positive entries, how many 0 are there, number of negative numbers
numbers = []
numsum = 0
positive = 0
negative = 0
zero = 0

print "Welcome to the number something tool\n"
num1 = input("Enter the 1st number:")
numbers.append(num1)
num2 = input("Enter the 2nd number:")
numbers.append(num2)
num3 = input("Enter the 3rd number:")
numbers.append(num3)
num4 = input("Enter the 4th number:")
numbers.append(num4)
num5 = input("Enter the 5th number:")
numbers.append(num5)
num6 = input("Enter the 6th number:")
numbers.append(num6)
num7 = input("Enter the 7th number:")
numbers.append(num7)

for num in numbers:
    numsum = numsum + num
    if num >0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero += 1

print ""
print "------ Results -----"
print "Total sum of the numbers:{}".format(numsum)
print "Total positive numbers:{}".format(positive)
print "Total negative numbers:{}".format(negative)
print "Total zero numbers:{}".format(zero)
