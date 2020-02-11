//////////////////////////////////////////////
//
// Matrix.h: interface for the CMatrix class.
//
//////////////////////////////////////////////

#if !defined(MATRIX_H)
#define MATRIX_H
class CMatrix{
  public:
    CMatrix(); //Default Construction
    CMatrix(int nRows, int nCols); //Specify row and column for Construction
    CMatrix(int nRows, int nCols, double value[]);//Specify datas for Constructor
    Cmatrix(int nSize);//Square matrix constructor
    Cmatrix(int nSize, double value[]);//Square matrix constructor
    CMatrix(const CMatrix& other);//Copied Construction
    virtual ~CMatrix();
    
  protected:
    int m_nNumColumns;
    int m_nNumRows;
    double* m_pData;
};
#endif //!defined(MATRIX_H)

