def addition(number_1, number_2):

def subtraction(number_1, number_2):

def multiplication(number_1, number_2):

def division(number_1, number_2):

def get_input():
	print("....SIMPLE CALCULATOR....")
	print("Select Operation\n1.Addition \n2.Substraction \n3.Multiplication \n 4.Division")
	number1=int(input("Enter the first number="))
	number2=int(input("Enter the second number="))
    option=int(input("Operation:"))
    if option ==1:
    	print("Addition of",number1,"and",number2,"=",addition(number1,number2))
    elif option==2:
    	print("Substraction of",number1,"and",number2,"=",substraction(number1,number2))
    elif option==3:
        print("Multiplication of",number1,"and",number2,"=",multiplication(number1,number2))
    elif option==4:
        print("Division of",number1,"and",number2,"=",division(number1,number2))
    else:
        print("Invalid input")


get_input()