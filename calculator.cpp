#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
return number_1+number_2;

}

int subtraction(int number_1, int number_2){

return number_1-number_2;
}

int multiplication(int number_1, int number_2){

return number_1*number_2;
}

int division(int number_1, int number_2){

if(number_2==0)
cout<<"DIVIDE BY ZERO ERROR";
else
return number_1/number_2;
}

int get_input(){
int operand1,operand2;
char operation;
cout<<"enter two operand or numbers for arthimetic operations";
cin>>operand1>>operand2;
cout<<"enter the operation to be performed";
cin>>operation;
switch(operation)
{
  case '+':{
             cout<<"the addition or sum is "<<addition(operand1,operand2);
             break;
           }
  case '-':{
             cout<<"the subtraction or difference is "<<subtraction(operand1,operand2);
             break;
           }
  case '*':{
             cout<<"the multiplication or product is "<<multiplication(operand1,operand2);
             break;
           }
  case '/':{
             cout<<"the division or quotient is "<<division(operand1,operand2);
             break;
           }
  default:{
            cout<<" enter the right operation to be performed";
            break;
          }
}

}

int main(){
    get_input();
    return 0;
} 

