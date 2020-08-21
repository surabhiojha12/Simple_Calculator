def addition(number_1, number_2):
  return number_1 + number_2

def subtraction(number_1, number_2):
  return number_1 - number_2

def multiplication(number_1, number_2):
  return number_1 * number_2

def division(number_1, number_2):
  try:
    return nuber_1 / number_2
  except:
    return 'cannot divide'
  
def get_input():
  data = input()
  if '+' in data:
    number_1, number_2 = [data.split('+')]
    print(addition(number_1, number_2)
  elif '-' in data:
    number_1, number_2 = [data.split('-')]
    print(addition(number_1, number_2)
  elif '*' in data:
    number_1, number_2 = [data.split('*')]
    print(addition(number_1, number_2)
  elif '/' in data:
    number_1, number_2 = [data.split('/')]
    print(addition(number_1, number_2)'
  else:
    print("wrong input")
          
 
get_input()


