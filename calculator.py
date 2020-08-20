def addition(number_1, number_2):
    return (number_1+number_2)

def subtraction(number_1, number_2):
    return (number_1-number_2)

def multiplication(number_1, number_2):
    return (number_1*number_2)

def division(number_1, number_2):
    try:
        return(number_1/number_2)
    except ZeroDivisionError:
        return 0
    


print("***SIMPLE CALCULATOR***")
print("Select Operation \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

opt=int(input("operation : "))

Number1=int(input("Enter the First Number = "))
Number2=int(input("Enter the Second Number = "))


if opt == 1:
     addition(Number1,Number2)
     print("Addition of ",Number1, " and",Number2 ," = ",addition(Number1,Number2))
     
elif opt == 2:
     print("Subtraction of ",Number1, " and",Number2, " = ", subtraction(Number1,Number2))
     
     
elif opt == 3:

    print("Multiplication of ",Number1, " and",Number2 ," = ", multiplication(Number1,Number2))
    
    
elif opt == 4:
   
    print("Division of ",Number1, " and",Number2, " = ", division(Number1,Number2))
    
else:
    print("Invalid input")
    
     
       