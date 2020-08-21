#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
       
    return number_1+number_2;

}

int subtraction(int number_1, int number_2){
    
     return  number_1-number_2;

}

int multiplication(int number_1, int number_2){
    number_1*number_2;
    return number_1*number_2;

}

int division(int number_1, int number_2){
    if(number_2==0)
        cout<<"Not defined"<<endl;
    else
        return number_1/number_2;

}

int get_input(){
    int number_1,number_2;
    cin>>number_1>>number_2;
    cout<<"Sum of two numbers number_1 and number_2 is: "<<addition(number_1,number_2)<<endl;
    cout<<"Difference of two numbers number_1 and number_2 is: "<<subtraction(number_1,number_2)<<endl;
    cout<<"Product of two numbers number_1 and number_2 is: "<<multiplication(number_1,number_2)<<endl;
    cout<<"Division of two numbers number_1 and number_2 is: "<<division(number_1,number_2)<<endl;
}

int main(){
    get_input();
    return 0;
}
