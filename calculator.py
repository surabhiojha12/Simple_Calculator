def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    return number_1 / number_2

print("Please select operation -\n")
print("1.Addition\n")
print("2.Subraction\n")
print("3.Multiplication\n")
print("4.Division\n")
def get_input():

    operation = int(input("Select an operation"))
    number_1 = int(input("Enter number_1: "))
    number_2 = int(input("Enter number_2: "))
    if operation == 1: 
        print(number_1, "+", number_2, "=", addition(number_1, number_2)) 
      
    elif operation == 2: 
        print(number_1, "-", number_2, "=", subtraction(number_1, number_2)) 
      
    elif operation == 3: 
        print(number_1, "*", number_2, "=", multiplication(number_1, number_2)) 
      
    elif operation == 4: 
        print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
    else: 
        print("Invalid input")

get_input()
