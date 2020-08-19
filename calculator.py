def addition(number_1, number_2):
    print('Addition:',number_1 + number_2)

def subtraction(number_1, number_2):
     print('Subtraction:',number_1 - number_2)

def multiplication(number_1, number_2):
     print('Multiplication:',number_1 * number_2)

def division(number_1, number_2):
     print('Division:',number_1 / number_2)

def get_input():
    global x, y
    x = int(input('Enter num1: '))
    y = int(input('Enter num2: '))

    
get_input()
addition(x, y)
subtraction(x, y)
multiplication(x, y)
division(x, y)
