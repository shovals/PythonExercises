bottles = 99

while bottles>0:
    print '{0} bottles of beer on the wall, {0} bottles of beer'.format(bottles)
    print 'Take one down, pass it around, {0} bottles of beer on the wall\n'.format(bottles-1)
    bottles -= 1
