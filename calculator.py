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
        num1 = float(input("Enter the first number : "))
        op = input("Enter the operation to be performed : ")
        num2 = float(input("Enter the second number : "))
    except :
        print("Enter a valid number/operator")
    else :
        if(op == '+') :
            print("\nAnswer :",addition(num1,num2))
        elif(op == '-') :
            print("\nAnswer :",subtraction(num1,num2))
        elif(op == '*') :
            print("\nAnswer :",multiplication(num1,num2))
        elif(op == '/') :
            ans = division(num1,num2)
            if(ans == None):
                print("\nYou can't divide a number by 0")
            else :
                print("\nAnswer :",ans)
        else :
            print("Enter an valid operation")

get_input()