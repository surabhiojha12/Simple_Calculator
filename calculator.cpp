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
int a,b;
cout<<"\n Enter two Integers :: ";
cin>>a>>b;
cout<<"\n Sum of Numbers "<<a<<" and "<<b <<" : "<<addition(a,b);
cout<<"\n Difference of Numbers "<<a<<" and "<<b <<" : "<<subtraction(a,b);
cout<<"\n Product of Numbers "<<a<<" and "<<b <<" : "<<multiplication(a,b);
if(b==0)
cout<<"\n Division Not Possible !!! Division by Zero error";
else
cout<<"\n Quotient of Division of Numbers "<<a<<" and "<<b <<" : "<<division(a,b);
}

int main(){
    get_input();
    return 0;
}
