import sys

def Fer2Cel(value):
    return (value-32)/1.8

def Cel2Fer(value):
    return value*1.8+32

UserInput = input('Enter a temperature: ')
Convert = raw_input('Convert to Cell (C) or Fer (F) ?')

if Convert == 'F':
    print UserInput, 'C is ', Fer2Cel(UserInput), 'in Fer'
else:
    print UserInput, 'F is ', Cel2Fer(UserInput), 'in Cel'
