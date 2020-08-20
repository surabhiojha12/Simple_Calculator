def addition(number_1, number_2):
 return number_1+number_2
def subtraction(number_1, number_2):
 return number_1-number_2
def multiplication(number_1, number_2):
 return number_1*number_2
def division(number_1, number_2):
 return number_1/number_2
def get_input():
    try:
        n1=float(input("Enter number one: "))
        op=input("Enter the operator: ")
        n2=float(input("Enter number two: "))
    except:
        print("Enter correct operator or value")
    else:
        if(op == '+') :
            print("\nAns :",addition(n1,n2))
        elif(op == '-') :
            print("\nAns :",subtraction(n1,n2))
        elif(op == '*') :
            print("\nAns :",multiplication(n1,n2))
        elif(op == '/') :
            Ans = division(n1,n2)
            if(Ans == None):
                print("\nIt is not possible to divide by 0")
            else :
                print("\nAns :",Ans)
        else :
            print("Enter an correct operator")
           

get_input()
input()

