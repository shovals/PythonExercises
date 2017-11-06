import sys
import os

filename = raw_input('Enter the file name: ')
print (open(filename).readlines()[-1])

