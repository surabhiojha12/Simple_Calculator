def addition(number_1, number_2):
    add =number_1+number_2;
    print("Addition of ",number_1," and ",number_2,"is:",add );
def subtraction(number_1, number_2):
    sub =number_1-number_2;
    print("Subtraction of ",number_1," and ",number_2,"is:",sub );
def multiplication(number_1, number_2):
    product =number_1*number_2;
    print("product of ",number_1," and ",number_2,"is:",product);
def division(number_1, number_2):
    if(number_2 != 0):
        quotient=number_1/number_2;
        print("Division of ",number_1," and ",number_2,"is:",quotient);
    else:
        print("Division cannot be done!");
def get_input():
    num=int(input());
    return num;

print("\t\t\t\tSIMPLE CALCULATOR\n");
print("Enter the first number:");
number_1=get_input();
print("Enter the second number:");
number_2=get_input();
c=int(input("Operations Available:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter you choice:"));
if(c==1):
    addition(number_1,number_2);
elif(c==2):
    subtraction(number_1,number_2);
elif(c==3):
    multiplication(number_1,number_2);
elif(c==4):
    division(number_1,number_2);
else:
    print("Invalid Choice!");
    
