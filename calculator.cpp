#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
return number_1 + number_2;
}

int subtraction(int number_1, int number_2){
return number_1 - number_2;
}

int multiplication (int number_1, int number_2){
return number_1*number_2;
}

int division(int number_1, int number_2){
return number_1/number_2;
}

int get_input(){
int number_1,number_2;
cout<<"\n Enter two Integers :: ";
cin>>number_1>>number_2;
cout<<"\n Sum of Numbers "<<number_1<<" and "<<number_2<<" : "<<addition(number_1,number_2);
cout<<"\n Difference of Numbers "<<number_1<<" and "<<number_2<<" : "<<subtraction(number_1,number_2);
cout<<"\n Product of Numbers "<<number_1<<" and "<<number_2<<" : "<<multiplication(number_1,number_2);
if(number_2==0)
cout<<"\n Division Not Possible !!! Division by Zero error";
else
cout<<"\n Quotient of Division of Numbers "<<number_1<<" and "<<number_2<<" : "<<division(number_1,number_2);
}

int main(){
    get_input();
    return 0;
}
