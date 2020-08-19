#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
return number_1 + number_2;
}

int subtraction(int number_1, int number_2){
return number_1 - number_2;
}

int multiplication(int number_1, int number_2){
return number_1*number_2;
}

int division(int number_1, int number_2){
return number_1/number_2;
}

int get_input(){
int number_1,number_2;
cout<<"\n Enter two Integers :: ";
cin>>number_1>>number_2;
cout<<"\n Sum of Numbers "<<number_1<<" and "<<number_2<<" : "<<addition(a,b);
cout<<"\n Difference of Numbers "<<number_1<<" and "<<number_2<<" : "<<subtraction(a,b);
cout<<"\n Product of Numbers "<<number_1<<" and "<<number_2<<" : "<<multiplication(a,b);
if(b==0)
cout<<"\n Division Not Possible !!! Division by Zero error";
else
cout<<"\n Quotient of Division of Numbers "<<number_1<<" and "<<number_2<<" : "<<division(a,b);
}

int main(){
    get_input();
    return 0;
}
