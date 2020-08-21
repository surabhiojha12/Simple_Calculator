def addition(number_1, number_2):
    sum = number_1 + number_2
    return sum

def subtraction(number_1, number_2):
    diff = number_1 - number_2
    return diff
    

def multiplication(number_1, number_2):
    mul = number_1 * number_2
    return mul    

def division(number_1, number_2):
    div = number_1 // number_2
    return div

def get_input():
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    return num1, num2

while(1):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    ch = int(input("Enter Choice"))
    if(ch == 5):
        break
    elif(ch < 5):
        num1, num2 = get_input()
        if(ch == 1):
            print("Sum : ", addition(num1, num2))
        elif(ch == 2):
            print("Differnce : ", subtraction(num1, num2))
        elif(ch == 3):
            print("Multiplication : ", multiplication(num1, num2))
        elif(ch == 4):
            print("Division : ", division(num1, num2))
