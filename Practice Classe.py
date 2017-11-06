class GetSomething(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = raw_input()

    def printUpperCase(self):
        print self.s.upper()

strObj = GetSomething()
strObj.getString()
strObj.printUpperCase()