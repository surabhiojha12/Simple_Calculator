#include<bits/stdc++.h>
using namespace std;

int addition(int number_1, int number_2){
      return number_1+ number_2;
}

int subtraction(int number_1, int number_2){
	return number_1-number_2;
}

int multiplication(int number_1, int number_2){
	return number_1*number_2;
}

int division(int number_1, int number_2){
	if(number_2==0)
	{
		cout<<"division by zero not possible";
		return 0;
	}
	else
		return number_1/number_2;
}

int get_input()
{
	int a,b;
	cout<<"ENTER TWO NUMBERS";
	cin>>a>>b;
	
	cout<<"addition of"<<a<<"and"<<b<<":"<<addition(a,b)<<"\n";
	cout<<"subraction of"<<a<<"and"<<b<<":"<<subraction(a,b)<<"\n";
	cout<<"multiplication of"<<a<<"and"<<b<<":"<<multiplication(a,b)<<"\n";
	cout<<"division of"<<a<<"and"<<b<<":"<<division(a,b);	
	
	return 0;
	
}

int main(){
    get_input();
    return 0;
}