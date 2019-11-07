#include<stdlib.h>
#include<stdio.h>
#include<math.h>

int main(){
 float shooterX[11] = { 0.15, 0.11, 0.04, 0.05, 0.04, 0.1, 0.1, 0.04, 0.05, 0.12, 0.2 };
 float shooterY[11] = { 0.01, 0.03, 0.05, 0.09, 0.11, 0.24, 0.21, 0.1, 0.1, 0.04, 0.02 };
 float mxX = 0;
 float mxY = 0;
 float dxX = 0;
 float dxY = 0;
 
 for(int i = 0; i < 11; i++){
    mxX = mxX + shooterX[i]*i;
    mxY = mxY + shooterY[i]*i;
    dxX = dxX + shooterX[i]*i*i;
    dxY = dxY + shooterY[i]*i*i;
 }
 
 dxX -=mxX*mxX;
 dxY -=mxY*mxY;
printf("|  xi  |");
 for(int i = 0; i < 11; i++){
     printf("|   %d  |", i);
 } 
 printf("\n|  pi  |");
 for(int i = 0; i < 11; i++){
     printf("| %.2f |", shooterX[i]);
 }
 

 printf("\n");
 printf("M1(x) = %.2f\nM2(x) = %.2f\nD1(x) = %.2f\nD2(x) = %.2f\n", mxX,mxY,dxX,dxY);

}