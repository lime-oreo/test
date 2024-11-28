//code
#include <stdio.h>
#include <stdbool.h>

bool test(int a)
{
    if (a%2==1) return true ;
    else return false;
}

int main ()
{
    int res = 0;
    int tmp;
    for (int i =0; i<6; i++)
    for (int j=0 ; j<6 ; j++)
    {

        if (test(i+j)) tmp = i;
        else tmp =0;
        res += tmp;    }
printf("%d",res);
return 0;
}


/*

*/