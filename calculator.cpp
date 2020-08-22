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
    if(number_2 == 0){
        cout<<" Division by 0 is not defined "<<end;
        return 0;
    }
    else{
        return number_1/number_2;
    }
}    

int get_input(){
    int number_1,number_2;
    cout<<"Enter 2 numbers"<<endl;
    cin>>number_1>>number_2;
    cout<<"addition : "<<addition(number_1,number_2)<<endl;
    cout<<"subtraction : "<<subtraction(number_1,number_2)<<endl;
    cout<<"multiplication : "<<multiplication(number_1,number_2)<<endl;
    cout<<"division : "<<division(number_1,number_2)<<endl;
    
}

int main(){
    get_input();
    return 0;
}
