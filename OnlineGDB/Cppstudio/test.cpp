//#include <stdio.h>
#include <iostream>
using namespace std;

//void func(int&, int&);
void func(int& a, int& b){
  int p;
  p = a;
  a = b;
  b = p;
}
int main(){
  int a = 0;
  int b = 1;
  func(a,b);
  cout<<"a="<<a<<",b="<< b<<endl;
  return 0;
}
