def addition(number_1, number_2):
    return(number_1+ number_2)

def subtraction(number_1, number_2):
    return(number_1 - number_2)

def multiplication(number_1, number_2):
    return(number_1 * number_2)

def division(number_1, number_2):
    return(number_1 // number_2)

print("SIMPLE CALCULATOR")
number_1=int(input("Enter First Number"))
number_2=int(input("Enter Second Number")) 


print("Select option: 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")

option=int(input("your option : "))

if(option==1):
   
    print("Addition of " ,number_1 ," and" ,number_2, " = ",addition(number_1, number_2))
    
elif(option==2):
   
     print("Additio of " ,number_1 ," and" ,number_2, " = ",subtraction(number_1, number_2))

elif(option==3):
     print("Additio of " ,number_1 ," and" ,number_2, " = ", multiplication(number_1, number_2))


elif(option==4):
    
    print("Additio of " ,number_1 ," and" ,number_2, " = ",division(number_1, number_2))
    
else:
    print("Invalid Input")
    


