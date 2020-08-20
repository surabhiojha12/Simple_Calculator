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
            print("Answer :",addition(number_1,number_2))
        elif(operator == '-') :
            print("Answer :",subtraction(number_1,number_2))
        elif(operator == '*') :
            print("Answer :",multiplication(number_1,number_2))
        elif(operator == '/') :
            answer = division(number_1,number_2)
            if(answer == None):
                print("You can't divide a number by 0")
            else :
                print("Answer :",answer)
        else :
            print("Enter an valid operation")

get_input()