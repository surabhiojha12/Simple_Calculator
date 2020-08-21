#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
    add = number_1 + number_2;
    cout<<add;

}

int subtraction(int number_1, int number_2){
    diff = number_1 - number_2;
    cout<<diff;

}

int multiplication(int number_1, int number_2){
    prod = number_1 * number_2;
    cout<<prod;

}

int division(int number_1, int number_2){
    div = number_1 / number_2;
    cout<<div;

}

int get_input(){
    char c;
    int number_1,number_2;
    cin>>c;
    cin>>number_1>>number_2;
    switch(c)
    {
        case '+': addition(number_1,number_2);
                   break;
        case '-': subtraction(number_1,number_2);
                   break;
        case '*': multiplication(number_1,number_2);
                   break;
        case '/': division(number_1,number_2);
                   break;
        default: cout<< "Invalid"
       
    }
        
}

int main(){
    get_input();
    return 0;
}
