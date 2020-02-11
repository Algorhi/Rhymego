#include <stdio.h>
#include <iostream>
#include "CComplex.h"
//不支持模板类的分类编译，所以要讲 包括进来，在原来的文件中#progma once
#include "CComplex.cpp"
#include <string>
using namespace std;

int main(){
  string s;
  CComplex<int> a(1,2);
  cout<<a.ToString()<<endl;
  printf("Done!");

  return 0;
}
