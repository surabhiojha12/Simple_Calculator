def addition(number_1, number_2):
    return number_1+number_2

def subtraction(number_1, number_2):
    return number_1-number_2

def multiplication(number_1, number_2):
    return number_1*number_2

def division(number_1, number_2):
    return number_1/number_2

print("Enter your Operation to be Performed :  ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
def get_input():
    while True:
        selection = input("Enter choice (1/2/3/4): ")
        if selection in('1','2','3','4'):
            x = int(input("Enter a number : "))
            y = int(input("Enter another number : "))
            if selection == '1':
                print(x,"+",y,"=",addition(x,y))
            elif selection == '2':
                print(x,"-",y,"=",subtraction(x,y))
            elif selection == '3':
                print(x,"*",y,"=",multiplication(x,y))
            elif selection == '4':
                print(x,"/",y,"=",division(x,y))
            break
        else:
            print("Enter a valid Operation")
get_input()

