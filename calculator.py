def addition(number_1, number_2):
    return number_1 + number_2

def subtraction(number_1, number_2):
    return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    if(number_2 ==0):
        return None
    else:
        return number_1 / number_2

def get_input():
    
     try:
    
        a=float(input("Enter first number : "))
        b=float(input("Enter second number: "))
        op= input("select the opertaion to be performed: '+','-','*','/' ")  

     except:
         print("Enter a valid number or operator")

     else: 
         if( op =='+'):
             print(a,"+",b, "=", addition(a,b))
             
         elif(op == '-'):
              print(a,"-",b, "=", subtraction(a,b))
              
         elif(op == '*'):
             print(a,"*",b,"=",multiplication(a,b))
             
         elif(op == '/'):
             ans = division(a,b)
             if(ans == None):
                 print("\nCannot divide a number by 0")
             else:
                 print(a,"/",b,"=",ans)
                 
         else:
             print("Enter an valid operator")

get_input()

                 
         
             
             

    
