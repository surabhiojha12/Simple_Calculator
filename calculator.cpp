#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
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

int get_input(){
 int number_1,number_2;
  char op;
  cout<<"enter operation";
  cin>>op;
 switch(op)
 {
    case '+': addition(number_1,number_2)
      break;
    case '-': subtraction(number_1,number_2)
       break;
    case '*': multiplication(number_1,number_2)
       break;
    case '/': division(number_1,number_2)
       break;
    default: cout<<"ERROR";
}

int main(){
    get_input();
    return 0;
}
