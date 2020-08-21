def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    return number_1/number_2

def get_input():
     return int(input())

a = get_input()
b = get_input()
print(addition(a,b))
print(subtraction(a,b))
print(multiplication(a,b))
print(division(a,b))


