def addition(number_1, number_2):
    return(number_1 + number_2)
def subtraction(number_1, number_2):
    return(number_1 - number_2)
def multiplication(number_1, number_2):
    return(number_1 * number_2)
def division(number_1, number_2):
    return(number_1 // number_2)
def get_input():
    number_1 = int(input())
    number_2 = int(input())
    return(number_1, number_2)

if __name__ == "__main__":
    number_1, number_2 = get_input()   
    print(addition(number_1, number_2))
    print(subtraction(number_1, number_2))
    print(multiplication(number_1, number_2))
    print(division(number_1, number_2))