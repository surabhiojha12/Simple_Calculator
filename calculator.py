def addition(number_1, number_2):
    a=number_1+number_2;
    print("Answer=",a);
def subtraction(number_1, number_2):
    a=number_1-number_2;
    print("Answer=",a);
def multiplication(number_1, number_2):
    a=number_1*number_2;
    print("Answer=",a);
def division(number_1, number_2):
    a=number_1/number_2;
    print("Answer=",a);
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
    
