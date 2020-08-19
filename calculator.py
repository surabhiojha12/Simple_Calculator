def addition(number_1, number_2):
    print(number_1+number_2)

def subtraction(number_1, number_2):
     print(number_1-number_2)

def multiplication(number_1, number_2):
     print(number_1*number_2)

def division(number_1, number_2):
    print(number_1/number_2)



print("1.addition 2.subtraction 3.multiplication 4.division")

ch=input("enter choice:")
number1=float(input("enter number 1:"))
number2=float(input("enter number 2:"))
if ch== "1":
    addition(number_1,number_2)
    

elif ch=="2":
    subtraction(number_1,number_2)
    
elif ch=="3":
    multiplication(number_1,number_2)
    
elif ch=="4":
    division(number_1,number_2)
    
else:
    print("Invalid input")
    
    

