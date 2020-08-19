def addition(number_1, number_2):
    print("sum of",number_1," and ",number_2," is ",(number_1 + number_2))

def subtraction(number_1, number_2):
    print("difference of",number_1," and ",number_2," is ",(number_1 - number_2))    


def multiplication(number_1, number_2):
    print("product of",number_1," and ",number_2," is ",(number_1 * number_2))  

def division(number_1, number_2):
    print("quotient of",number_1," and ",number_2," is ",(number_1 // number_2))  

def get_input():
    global a 
    global b
    a = float(input("enter the first number: "))
    b = float(input("enter the second number: "))

print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION")
n = int(input("enter the option: "))
get_input()
if(n == 1):
    addition(a,b)
elif(n == 2):
    subtraction(a,b)
elif(n == 3):
    multiplication(a,b)
elif(n == 4):
    division(a,b)
else:
    print("INVALID OPTION")




