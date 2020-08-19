#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
    return number_1 + number_2;
}

int subtraction(int number_1, int number_2){
    return number1 - number2;
}

int multiplication(int number_1, int number_2){
    return number_1*number_2;
}

int division(int number_1, int number_2){
    return number_1/number_2;
}

int get_input(){
    int a,b;
    cout<<"Enter 2 numbers"<<endl;
    cin>>a>>b;
    cout<<"addition : "<<addition(a,b)<<endl;
    cout<<"subtraction : "<<subtraction(a,b)<<endl;
    cout<<"multiplication : "<<multiplication(a,b)<<endl;
    cout<<"division : "<<division(a,b)<<endl;
    
}

int main(){
    get_input();
    return 0;
}
