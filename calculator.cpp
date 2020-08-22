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
int n1,n2,ans;
    cin>>n1>>n2;
    ans=addition(n1,n2);
    cout<<"\nthe sum of the 2 nos. is "<<ans;
    ans=subtraction(n1,n2);
    cout<<"\nthe difference of 2 nos. is "<<ans;
    ans=multiplication(n1,n2);
    cout<<"\nthe product of 2 nos. is "<<ans;
    ans=division(n1,n2);
    cout<<"\nthe quotient of the 2 nos. is "<<ans;
    return 0;
}

int main(){
    get_input();
    return 0;
}
