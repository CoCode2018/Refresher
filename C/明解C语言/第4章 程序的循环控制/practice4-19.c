#include <stdio.h>

int main(void)
{
    int num;
    int cont = 0;
    printf("整数值: ");    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        if( num % i == 0){
            printf("%d\n", i);
            cont++;
        }
    }
    printf("约数有%d个。\n", cont);
    return 0;
}