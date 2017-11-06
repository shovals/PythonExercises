class InputOutputString(object):
    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = raw_input()

    def printString(self):
        print self.s.upper()

name = InputOutputString()
name.getString()
name.printString()