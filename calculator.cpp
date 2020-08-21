#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
     return number_1+number_2;
}

int subtraction(int number_1, int number_2){
    return number_1 - number_2;
}

int multiplication(int number_1, int number_2){
    return number_1 * number_2;
}

int division(int number_1, int number_2){
    if(number_2 != 0)
        return number_1 / number_2;
     else
          cout <<"Division by zero is not possible"<<endl; 
}

int get_input(){
    int number_1,number_2;
    cout<<"Enter a and b"<<endl;
    cin>>number_1>>number_2;
    cout<<"Sum:";
    cout<<addition(number_1,number_2)<<endl;
    cout<<"Differnence:";
    cout<<subtraction(number_1,number_2)<<endl;
    cout<<"Product:";
    cout<<multiplication(number_1,number_2)<<endl;
    cout<<"Division:";
    cout<<division(number_1,number_2)<<endl;
}

int main(){
    get_input();
    return 0;
}
