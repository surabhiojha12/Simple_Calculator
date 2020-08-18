def addition(number_1, number_2):
  print("=",number_1+number_2)

def subtraction(number_1, number_2):
   print("=",number_1-number_2)

def multiplication(number_1, number_2):
   print("=",number_1*number_2)

def division(number_1, number_2):
   print("=",number_1/number_2)

def get_input():
  print("Enter num1 operator num2")
  num1=input(int)
  op=input(char)
  numb2=input(int)
  if(op=='+'):
  addition(num1,num2)
  elif(op=='-'):
  subtraction(num1,num2)
  elif(op=='*'):
  multiplication(num1,num2)
  elif(op=='/'):
  division(num1,num2)
  

get_input()
