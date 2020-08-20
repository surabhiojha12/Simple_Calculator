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
    return number_1/number_2;
    

}

int get_input(){
    return 6;

}

int main(){
    int a,b;
    get_input(a);
    get_input(b);
    cout<<addition(a,b)<<"\n";
    cout<<subractin(a,b)<<"\n";
    cout<<multiplication(a,b)<<"\n";
    cout<<division(a,b)<<"\n";
    
    return 0;
}
