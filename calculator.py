def addition(number_1,number_2):
    sum=number_1+number_2
    print("Sum of",number_1,"and",number_2,"is:",sum)

def subtraction(number_1,number_2):
    difference=number_1-number_2
    print("Difference of",number_1,"and",number_2,"is:",difference)

def multiplication(number_1,number_2):
    product=number_1*number_2
    print("Product of",number_1,"and",number_2,"is:",product)
    
def get_input():
    number_1=int(input("Enter the first number: "))
    number_2=int(input("Enter the second number: "))
    print("Select any operation")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input())
    if choice==1:
        addition(number_1,number_2)
    elif choice==2:
        subtraction(number_1,number_2)
    elif choice==3:
        multiplication(number_1,number_2)
    elif choice==4:
        division(number_1,number_2)
    else:
        print("Invalid Option")

get_input()
    

