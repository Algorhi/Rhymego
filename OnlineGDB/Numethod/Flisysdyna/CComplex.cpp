#pragma once
#include<iostream>
#include"CComplex.h"

using namespace std;
template<typename T>
CComplex<T>::CComplex(T re, T im):real(re),image(im){
  cout<<"c"<<endl;
}
template<typename T>
CComplex<T>::CComplex(const CComplex& a):real(a.real),image(a.image){
}
