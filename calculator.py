def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    if(number_2 == 0):
        return None
    else :
        return number_1 / number_2

def get_input():
    try : 
        number_1 = float(input("Enter the first number : "))
        operator = input("Enter the operation to be performed : ")
        number_2 = float(input("Enter the second number : "))
    except :
        print("Enter a valid number/operator")
    else :
        if(operator == '+') :
            print(f"{number_1} + {number_2} = {addition(number_1,number_2)}")
        elif(operator == '-') :
            print(f"{number_1} - {number_2} = {subtraction(number_1,number_2)}")
        elif(operator == '*') :
            print(f"{number_1} * {number_2} = {multiplication(number_1,number_2)}")
        elif(operator == '/') :
            division_result = division(number_1,number_2)
            if(division_result == None):
                print("You can't divide a number by 0")
            else :
                print(f"{number_1} / {number_2} = {division_result}")
        else :
            print("Enter an valid operation")

get_input()