def addition(number_1, number_2):
  print(number_1,"+",number_2,"=",(number_1+number_2))
def subtraction(number_1, number_2):
  print(number_1,"-",number_2,"=",(number_1-number_2))

def multiplication(number_1, number_2):
  print(number_1,"*",number_2,"=",(number_1*number_2))

def division(number_1, number_2):
  print(number_1,"/",number_2,"=",(number_1/number_2))

def get_input():
  number_1=int(input())
  number_2=int(input())
  operator=str(input())
  if(operator=="+"):
    addition(number_1,number_2)
  elif(operator=="-"):
    subtraction(number_1,number_2)
  elif(operator=="*"):
    multiplication(number_1,number_2)
  elif(operator=="/"):
    division(number_1,number_2)

get_input()
