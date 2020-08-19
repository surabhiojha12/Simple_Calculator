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
int ch,a,b;
cout<<"enter a choice";
cin>>ch;
switch(ch)
{
 case 1:{ cin>>a>>b;
          cout<<addition(a,b);
          break;
        }
 case 2:{ cin>>a>>b;
          cout<<subtraction(a,b);
          break;
        }
 case 3:{ cin>>a>>b;
          cout<<multiplication(a,b);
          break;
        }
 case 4:{ cin>>a>>b;
          cout<<division(a,b);
          break;
        }
}

int main(){
    get_input();
    return 0;
}
