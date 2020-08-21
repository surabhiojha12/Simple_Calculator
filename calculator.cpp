#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
    int c;
    c=number_1+number_2;
    return c;

}

int subtraction(int number_1, int number_2){
     int d;
     d=number_1-number_2;
     return d;

}

int multiplication(int number_1, int number_2){
    int e;
    e=number_1*number_2;
    return e;

}

int division(int number_1, int number_2){
    int f;
    f=number_1/number_2;
    return f;

}

int get_input(){
    int x,y;
    cin>>x>>y;
    cout<<addition(x,y)<<endl;
    cout<<subtraction(x,y)<<endl;
    cout<<multiplication(x,y)<<endl;
    cout<<division(x,y)<<endl;
}

int main(){
    get_input();
    return 0;
}
