def addition(number_1, number_2):
    print("sum of",number_1," and ",number_2," is ",(number_1 + number_2))

def subtraction(number_1, number_2):
    print("difference of", number_1, " and ", number_2, " is ", (number_1 - number_2))

def multiplication(number_1, number_2):
    print("product of", number_1, " and ", number_2, " is ", (number_1 * number_2))

def division(number_1, number_2):
    print("quotient of", number_1, " and ", number_2, " is ", (number_1 // number_2))

print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION")
n = int(input("enter the option: "))
number_1 = int(input("enter the first number: "))
number_2 = int(input("enter the second number: "))
if(n == 1):
    addition(number_1,number_2)
elif(n == 2):
    subtraction(number_1,number_2)
elif(n == 3):
    multiplication(number_1,number_2)
elif(n == 4):
    division(number_1,number_2)
else:
    print("INVALID OPTION")