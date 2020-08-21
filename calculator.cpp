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
    int a;
    cin>>a;
    return a ;

}

int main(){
   int input1,input2;
    input1=get_input();
    b=get_input();
    cout<<addition(input1,input2)<<"\n ";
    cout<<subractin(input1,input2)<<"\n";
    cout<<multiplication(input1,input2)<<"\n";
    cout<<division(input1,input2)<<"\n";
    
    return 0;
}
