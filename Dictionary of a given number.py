# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.

if __name__ == '__main__':
    Dic = {}
    Number = raw_input('Enter a number please: ')
    for i in range(1, int(Number)+1):
        Dic[i]=i*i

print Dic
