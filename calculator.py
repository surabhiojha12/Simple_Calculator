def addition(number_1, number_2):
  print(number_1,"+",number_2,"=",(number_1+number_2))

def subtraction(number_1, number_2):
  print(number_1,"-",number_2,"=",(number_1-number_2))

def multiplication(number_1, number_2):
  print(number_1,"*",number_2,"=",(number_1*number_2))
  
def division(number_1, number_2):
  print(number_1,"/",number_2,"=",(number_1/number_2))

def get_input():
  a=int(input())
  b=int(input())
  c=str(input())
  if(c=="+"): 
    addition(a,b)
  elif(c=="-"):
    subtraction(a,b)
  elif(c=="*"):
    multiplication(a,b)
  elif(c=="/"):
    division(a,b)

get_input()
