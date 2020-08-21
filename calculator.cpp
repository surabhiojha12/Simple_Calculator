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
	int number_1,number_2;
	cout<<"ENTER TWO NUMBERS";
	cin>>number_1>>number_2;
	
	cout<<"addition of"<<number_1<<"and"<<number_2<<":"<<addition(number_1,number_2)<<"\n";
	cout<<"subraction of"<<number_1<<"and"<<number_2<<":"<<subtraction(number_1,number_2)<<"\n";
	cout<<"multiplication of"<<number_1<<"and"<<number_2<<":"<<multiplication(number_1,number_2)<<"\n";
	cout<<"division of"<<number_1<<"and"<<number_2<<":"<<division(number_1,number_2);	
	
	return 0;
	
}

int main(){
    get_input();
    return 0;
}