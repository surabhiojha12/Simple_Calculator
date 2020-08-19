def addition(number_1, number_2):
  print(number_1,"+",number_2,"=",number_1+number_2)

def subtraction(number_1, number_2):
  print(number_1,"-",number_2,"=",number_1-number_2)

def multiplication(number_1, number_2):
  print(number_1,"*",number_2,"=",number_1*number_2)

def division(number_1, number_2):
  if(number_2!=0):
     print(number_1,"/",number_2,"=",number_1/number_2)
  print(number_1,"/",number_2,"= not defined")
  

def get_input():
  print("Enter number1 followed by operator and then number2")
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
  
input()
get_input()
