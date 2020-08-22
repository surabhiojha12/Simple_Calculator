n1=int(input("Enter the number 1 : "))
n2=int(input("Enter the number 2 : "))
print("Enter the Operation : \n "\"1-Addition\n"\"2-Multiplication\n"\"3-Division\n")
op=int(input("Enter the option from 1 to 4"))
if op==1:
   print(n1," + ",n2," = ",n1+n2)
elif op==2:
   print(n1," - ",n2," = ",n1-n2)
elif op==3:
   print(n1," x ",n2," = ",n1*n2)
elif op==4:
   print(n1," / ",n2," = ",n1/n2)
