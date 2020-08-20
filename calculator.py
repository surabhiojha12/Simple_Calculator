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
        number1 = float(input("Enter the first number : "))
        operator = input("Enter the operation to be performed : ")
        number2 = float(input("Enter the second number : "))
    except :
        print("Enter a valid value/operator")
    else :
        if(operator == '+') :
            print("\nAnswer :",addition(number1,number2))
        elif(operator == '-') :
            print("\nAnswer :",subtraction(number1,number2))
        elif(operator == '*') :
            print("\nAnswer :",multiplication(number1,number2))
        elif(operator == '/') :
            answer = division(number1,number2)
            if(answer == None):
                print("\nYou cannot divide a number by 0 since it is not defined")
            else :
                print("\nAnswer :",answer)
        else :
            print("Enter an valid operation")

get_input()

input()

