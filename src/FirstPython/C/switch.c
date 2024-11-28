#include <stdio.h>
int main(){
    int num;
    scanf("%d",&num); //& num 주소값을 받아오는것 . input과 동일
    switch (num) {
    case 1:
        printf("type 1\n");
        break;
    case 2:
        printf("type 2\n");
        break;
    case 3:
        printf("type 3\n");
        break;
    default:
        printf("type error\n");
        break;
    
    
    }
    return 0;

}