#pragma once
#include<string>
template<typename T>
class CComplex{
  public:
    CComplex(T re=0,T im=0);
    CComplex(const CComplex&);
    virtual ~CComplex();

    void SetReal(T);
    void SetImag(T);
    T GetReal() const;
    T GetImag() const;
    std::string ToString() const;
    // void FromString(CString,const CString&);
    //
    // bool operator!=(const CComplex&) const;

  private:
    T real,image;

};


