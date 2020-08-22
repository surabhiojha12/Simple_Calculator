#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
	int add;
	add=number_1+number_2;
	cout<<add;
	return 0;
}

int subtraction(int number_1, int number_2){
	int sub;
	sub=number_1-number_2;
	cout<<sub;
	return 0;
}

int multiplication(int number_1, int number_2){
	int mul;
	mul=number_1*number_2;
	cout<<mul;
	return 0;
}

int division(int number_1, int number_2){
	int div;
	div=number_1/number_2;
	cout<<div;
	return 0;
}

int get_input(){
    int num1,num2;
	char operation;
	cin>>num1;
	cin>>num2;
	cout<<"Enter operation to be performed\n";
	cin>>operation;
	switch(operation)
	{
		case '+':
		addition(num1,num2);
		break;
		case '-':
		subtraction(num1,num2);
		break;
		case '*':
		multiplication(num1,num2);
		break;
		case '/':
	       	if(num1==0||num2==0)
	        {
	        	cout<<"Enter valid number\n";
	        	exit(0);
        	}
		division(num1,num2);
		break;
	}	
}

int main(){
  	get_input();
    return 0;
}
