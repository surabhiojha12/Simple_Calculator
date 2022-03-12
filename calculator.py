def addition(number_1, number_2):
    return number_1+number_2

def subtraction(number_1, number_2):
    return number_1-number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    if number_2 == 0:
        return("Zero Division Error")
    return number_1/number_2

def get_input():
    m,n=input().split()
    number1 = int(m)
    number2 = int(n)
    print("Addition is: ",addition(number1,number2))
    print("Subtraction is: ",subtraction(number1,number2))
    print("Multiplication is: ",multiplication(number1,number2))
    print("Division is: ",division(number1,number2))

get_input()
    
