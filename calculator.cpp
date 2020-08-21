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
    return number_1 / number_2;
}

int get_input(){
    int a,b;
    cout<<"Enter a and b"<<endl;
    cin>>a>>b;
    cout<<"Sum:";
    cout<<addition(a,b)<<endl;
    cout<<"Differnence:";
    cout<<subtraction(a,b)<<endl;
    cout<<"Product:";
    cout<<multiplication(a,b)<<endl;
    cout<<"Division:";
    cout<<division(a,b)<<endl;
}

int main(){
    get_input();
    return 0;
}
