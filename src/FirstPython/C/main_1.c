#include <stdio.h>

int printBin(int a)
{
    if (a==0 | a==1) printf("%d",a);
    else
    {
        printBin(a/2);
        printf("%d",a%2);
    }
}

int main()
{
    int x = 11;
    printBin(x);
    return 0;
}

/* ----------------------------------------*/
/*
x= 11
printBin(11) > a = 11
 
 | 합집합인데? 

 11/2 >5.5 , 5.5/2 = 1.5?


*/

