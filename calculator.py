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
    num_1 = int(input('Enter num1: '))
    num_2 = int(input('Enter num2: '))
    return (num_1, num_2)

def calculator():

     num1, num2 = get_input()
     addition(num1, num2)
     subtraction(num1, num2)
     multiplication(num1, num2)
     division(num1, num2)

calculator()
