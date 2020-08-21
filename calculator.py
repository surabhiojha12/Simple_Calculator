def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    return number_1 / number_2
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if choice == '1':
                print(number_1, "+", number_2, "=", addition(number_1, number_2))

            elif choice == '2':
                print(number_1, "-", number_2, "=", subtraction(number_1, number_2))

            elif choice == '3':
                print(number_1, "*", number_2, "=", multiplication(number_1, number_2))

            elif choice == '4':
                print(number_1, "/", number_2, "=", division(number_1, number_2))
            break
        else:
            print("Invalid Input")
        

