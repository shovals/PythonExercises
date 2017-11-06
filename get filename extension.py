# get filename from user and print the file extension

import os

path = raw_input('Enter full filename:')
path = path.split('.')

print path[-1]