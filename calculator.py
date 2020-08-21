def addition(number_1, number_2):
    return number_1+number_2
def subtraction(number_1, number_2):
    return number_1-number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    return number_1/number_2

def get_input():
    list=[]
    list=input().split()
    print(addition(int(list[0]),int(list[1])))
    print(subtraction(int(list[0]),int(list[1])))
    print(multiplication(int(list[0]),int(list[1])))
    input(division(int(list[0]),int(list[1])))
    
get_input()
