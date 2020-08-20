def addition(number_1, number_2):
  result=number_1+number_2
  print(number_1,"+",number_2,"=",result)
def subtraction(number_1, number_2):
  result=number_1-number_2
  print(number_1,"-",number_2,"=", result)

def multiplication(number_1, number_2):
  result=number_1*number_2
  print(number_1,"*",number_2,"=", result)

def division(number_1, number_2):
  return(number_1/number_2)

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
    try:
      result=division(number_1,number_2)
      print(number_1,"/", number_2,"=",result)
    except ZeroDivisonError as error:
      print(error) 
      
    

get_input()
