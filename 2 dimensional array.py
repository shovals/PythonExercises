# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

if __name__ == '__main__':
    value = []
    digits = [x for x in raw_input('Enter a list of numbers: ').split(',')]
    for d in digits:
        value.append(d)

    print ','.join(value)
