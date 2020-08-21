def addition(number_1, number_2):
    print("the sum is"+(number_1+number_2)
def subtraction(number_1, number_2):
    print("the difference is"+(number_1-number_2)

def multiplication(number_1, number_2):
    print("the product is"+(number_1*number_2)

def division(number_1, number_2):
    print("the  is"+(number_1+number_2)

def get_input():
    a=int()
    b=int()
    a=input()
    b=input()
    if(a!=0 and b!=0):
        addition(a,b)
        subtraction(a,b)
        multiplication(a,b)
        division(a,b)
get_input()
