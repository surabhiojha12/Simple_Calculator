def addition(number_1, number_2):
    print('Addition:',number_1 + number_2)

def subtraction(number_1, number_2):
     print('Subtraction:',number_1 - number_2)

def multiplication(number_1, number_2):
     print('Multiplication:',number_1 * number_2)

def division(number_1, number_2):
     if number_2 == 0:
          print("Division: Undefined")
     else:
          print('Division:',number_1 / number_2)

def get_input():
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    return (num1, num2)

def calculator():

     x, y = get_input()
     addition(x, y)
     subtraction(x, y)
     multiplication(x, y)
     division(x, y)

calculator()
