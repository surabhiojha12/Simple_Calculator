def addition(number_1, number_2):
    return (number_1+number_2)

def subtraction(number_1, number_2):
    return (number_1-number_2)

def multiplication(number_1, number_2):
    return (number_1*number_2)

def division(number_1, number_2):
    return(number_1/number_2)


#select option

print("***SIMPLE CALCULATOR***")
print("Select Operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

opt=int(input("operation : "))

Number1=int(input("Enter the First Number = "))
Number2=int(input("Enter the Second Number = "))
int result

if opt == 1:
     result=addition(Number1,Number2)
     print("Addition of ",Number1, " and",Number2 " = "result)
     
else if opt == 2:
     result=subtraction(Number1,Number2)
     print("Subtraction of ",Number1, " and",Number2 " = "result)
     
     
else if opt == 3:
    result=multiplication(Number1,Number2)
    print("Multiplication of ",Number1, " and",Number2 " = "result)
    
    
else if opt == 4:
    result=division(Number1,Number2)
    print("Division of ",Number1, " and",Number2 " = "result)
    
else:
    print("Invalid input")
    
     
       