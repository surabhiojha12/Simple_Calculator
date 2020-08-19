def addition(number_1, number_2):
    add = number_1 + number_2
    print("sum is ",add)

def subtraction(number_1, number_2):
    sub = number_1 - number_2
    print("difference is ",sub)

def multiplication(number_1, number_2):
    mul = number_1 * number_2
    print("product is ",mul)

def division(number_1, number_2):
    div = number_1 // number_2
    print("quotient is ",div)

number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))
print("1 - add\t 2 - sub\t 3 - multiply\t 4 - divide")
a = int(input("enter the option: "))
if(a == 1):
    addition(number_1,number_2)
elif(a == 2):
    subtraction(number_1,number_2)



