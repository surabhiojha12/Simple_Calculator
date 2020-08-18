def addition(number_1, number_2):
    return number_1+number_2
def subtraction(number_1, number_2):
    return number_1-number_2
def multiplication(number_1, number_2):
    return number_1*number_2
def division(number_1, number_2):
    return number_1/number_2
def get_input():
    num1, operate, num2 = input().split()
    num1=int(num1)
    num2=int(num2)
    if(operate=='+'):
        print(addition(num1,num2))
    if(operate=='-'):
        print(subtraction(num1,num2))
    if(operate=='*'):
        print(multiplication(num1,num2))
    if(operate=='/'):
        print(division(num1, num2))
get_input()
