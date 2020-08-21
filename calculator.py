def addition(number_1, number_2):
  return number_1 + number_2

def subtraction(number_1, number_2):
  return number_1 - number_2
  
def multiplication(number_1, number_2):
  return number_1 * number_2
  
def division(number_1, number_2):
  return number_1 / number_2
  
def get_input():
  print("select operation")
  print("+")
  print("-")
  print("*")
  print("/")
  operator = input("Enter the operator to be used")
  number_1=int(input("Enter first number"))
  number_2=int(input("Enter second number"))
  if (operator=='+'):
      print(number_1,"+",number_2,"=",addition(number_1,number_2))
  elif (operator=='-'):
      print(number_1,"-",number_2," =",subtraction(number_1,number_2))
  elif (operator=='*'):
      print(number_1,"*",number_2,"=",multiplication(number_1,number_2))
  elif (operator=='/'):
      print(number_1,"/",number_2,"=",division(number_1,number_2))
  else:
      print("invalid")
    
  
  
 get_input()
