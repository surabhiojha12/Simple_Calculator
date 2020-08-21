def addition(number_1, number_2):
    return number_1+number_2
def subtraction(number_1, number_2):
    return number_1-number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    if(number_2==0):
        return "zero division error"
    else:
        return number_1/number_2

def get_input():
    number_1=int(input("Enter 1st number :: "))
    number_2=int(input("Enter second number :: "))
    print("Addition :: "+str(addition(number_1,number_2)))
    print("Subtraction :: "+str(subtraction(number_1,number_2)))
    print("Multiplication :: "+str(multiplication(number_1,number_2)))
    print("Division :: "+str(division(number_1,number_2)))
    
get_input()
