/******************************************
Flisysdyna: Flight System Dynamics Simulation
******************************************/

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include "Mathkit.h"
#include "RunFlight.h"

#include "Matrix.h"
using namespace std;
using namespace mathkit;
int main(){
  double ys[] = {4,9,16,25};
  Cmatrix M(2,2,ys);
  Cmatrix C = M.Pow(0.5);
  Cmatrix TD = M.Transpose();
  Cmatrix TD = TD.GetTransposed();
  //GetTransposed Transpose
  int rank = C.rank();
  printf("%d\n",rank);


  for (int i = 0;i < 4; i++)
    cout << " y(" << i << " ) = " << setw(8) << *(TD.GetData() + i);
  printf("\n%f\n",*(C.GetData() + 1));
}
