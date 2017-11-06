from Calculator import Calc

if __name__ == "__main__":
    print 'Welcome to the greatest calc of all'
    Num1 = input('Enter the first number: ')
    Num2 = input('Enter the second number: ')

    print Num1, '+', Num2, '=', Calc.add(Num1, Num2)
    print Num1, '/', Num2, '=', Calc.divide(Num1, Num2)
    print Num1, '*', Num2, '=', Calc.multiply(Num1, Num2)
    print Num1, '-', Num2, '=', Calc.subtract(Num1, Num2)
    print Num1, '^2', '=', Calc.sqrt(Num1)

    print 'Yea Baby :-)' #TODO think of more austin sentences


