def addition(number_1, number_2):
    return number_1+number_2

def subtraction(number_1, number_2):
    return number_1-number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    return number_1/number_2

def get_input():
    m,n=input().split()
    print(addition(int(m),int(n)))
    print(subtraction(int(m),int(n)))
    print(multiplication(int(m),int(n)))
    print(division(int(m),int(n)))

get_input()
    
