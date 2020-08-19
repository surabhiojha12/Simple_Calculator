def addition(number_1, number_2):
  return(number_1+number_2)

def subtraction(number_1, number_2):
  return(number_1-number_2)

def multiplication(number_1, number_2):
  return(number_1*number_2)

def division(number_1, number_2):
  return(number_1/number_2)

def get_input():
  number_1=int(input())
  number_2=int(input())
  operator=str(input())
  if(operator=="+"):
    answer= addition(number_1,number_2)
    print(number_1,"+",number_2,"=",answer)
  elif(operator=="-"):
    answer= subtraction(number_1,number_2)
    print(number_1,"-",number_2,"=",answer)
  elif(operator=="*"):
    answer= multiplication(number_1,number_2)
    print(number_1,"*",number_2,"=",answer)
  elif(operator=="/"):
    try:
      answer=division(number_1,number_2)
      print(number_1,"/",number_2,"=",answer)
    except ZeroDivisionError as error:
      print(error)
get_input()
