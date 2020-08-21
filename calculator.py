def addition(number_1, number_2):
    print(number_1,"+",number_2,"=",number_1+number_2)

def subtraction(number_1, number_2):
    print(number_1,"-",number_2,"=",number_1-number_2)

def multiplication(number_1, number_2):
    print(number_1,"*",number_2,"=",number_1*number_2)

def division(number_1, number_2):
    if(number_2!=0):
        print(number_1,"/",number_2,"=",number_1/number_2)
    else:
        print(number_1,"/",number_2,"= not defined")


def get_input():
    print("Enter the numbers for calculation number1 & number2")
    num1=input(int)
    num2=input(int)
    print("\n Enter '1' for adition \n '2' for subraction \n '3' for multiplication \n '4' for division \n")    
    op = int(input()) 

    if(op=='+'):
        addition(num1,num2)

    elif(op=='-'):
        subtraction(num1,num2)
    
    elif(op=='*'):
        multiplication(num1,num2)
    
    elif(op=='/'):
        division(num1,num2)
    
input()
get_input()