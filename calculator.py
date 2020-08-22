def addition(number_1, number_2):
    Sum = number_1 + number_2
    Sum = int(Sum)
    print("Addition of " , number_1 , " and " , number_2 , " is " , Sum)

def subtraction(number_1, number_2):
    Sub = number_1 - number_2
    Sub = int(Sub)
    print("Subtraction of " , number_1 , " and " , number_2 , " is " , Sub)

def multiplication(number_1, number_2):
    Mul = number_1 * number_2
    Mul = int(Mul)
    print("Multiplication of " , number_1 , " and " , number_2 , " is " , Mul)
    
def division(number_1, number_2):
    if number_2 != 0 :
        Div = number_1 / number_2
        Div = int(Div)
        print("Division of " , number_1 , " and " , number_2 , " is " , Div)
    else :
        print("Divisor can't be 0 \n")
    

def get_input():
    number = int(input())
    return number

print("\t\t\t Calculator\n")
print("Enter number 1 : ")
number_1 = get_input()
print("Enter number 2 : ")
number_2 = get_input()
print("1. Add 2. Sub 3. Mul 4. Div")
i = get_input()
if i == 1 :
    addition(number_1, number_2)
elif i == 2 :
    subtraction(number_1, number_2)
elif i == 3 :
    multiplication(number_1, number_2)
elif i == 4 :
    division(number_1, number_2)
else :
    print("Invalid Choice")
