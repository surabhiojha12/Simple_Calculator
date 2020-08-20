def addition(number_1, number_2):
  return number_1+number_2

def subtraction(number_1, number_2):
  return number_1-number_2

def multiplication(number_1, number_2):
   return number_1*number_2

def division(number_1, number_2):
   return number_1/number_2

def get_input():
    global x,y,op     
    x = int(input("Enter num1 :"))
    op = input("Operator (+, -, *, /):")
    y = int(input("Enter num2 :"))

get_input()

if op == "+":
    print("Answer : ",addition(x,y))
elif op == "-":
    print("Answer : ",subtraction(x,y))
elif op == "*":
    print("Answer : ",multiplication(x,y))
elif op == "/":
    print("Answer : ",division(x,y))
