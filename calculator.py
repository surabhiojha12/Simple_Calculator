def addition(number_1, number_2):
  print(number_1 + number_2)

def subtraction(number_1, number_2):
  print(number_1 - number_2)

def multiplication(number_1, number_2):
  print(number_1 * number_2)

def division(number_1, number_2):
  print(number_1 / number_2)

def get_input():
  a,b,c = input().split()
  a=int(a)
  c=int(c)
  if(b == '+'):
    addition(a,c)
  elif(b == '-'):
    subtraction(a,c)
  elif(b == '*'):
    multiplication(a,c)
  elif(b == '/'):
    division(a,c)
  else:
    print("invalid input")

get_input()
