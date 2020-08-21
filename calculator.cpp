#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2)
{
cout<<number_1+number_2;
}

int subtraction(int number_1, int number_2){
cout<<number_1-number_2;
}

int multiplication(int number_1, int number_2){
cout<<number_1*number_2;
}

int division(int number_1, int number_2){
cout<<number_1/number_2;
}

int get_input(){ int input1,input2; char choice;
cin<<input1;
cin<<input2;
cin<<choice;
                switch(choice)
                { case '+': addition(input1,input2);
                            break;
                 case '-': subtraction(input1, input2);
                            break;
                 case '*': multiplication(input1, input2);
                            break;
                 case '/': division(input1,input2);
                            break;
                 default: cout<<"ERROR";
                }
}

int main(){
    get_input();
    return 0;
}
