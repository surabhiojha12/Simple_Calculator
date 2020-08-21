#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){

cout<<"Addition: "<<number_1+number_2;
return 0;
}

int subtraction(int number_1, int number_2){

cout<<"\nSubtraction: "<<number_1-number_2;
return 0;
}

int multiplication(int number_1, int number_2){

cout<<"\nMultiplication: "<<number_1+number_2;
return 0;
}

int division(int number_1, int number_2){

cout<<"\nDivision: "<<number_1+number_2;
return 0;
}

int get_input(){

float num1,num2;
cin>>num1>>num2;
addition(num1,num2);
subtraction(num1,num2);
multiplication(num1,num2);
division(num1,num2);
return 0;
}

int main(){
    get_input();
    return 0;
}