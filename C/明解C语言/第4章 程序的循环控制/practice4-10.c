#include <stdio.h>

int main(void)
{
    int num;
    printf("正整数:  ");    scanf("%d", &num);

    while(num-- > 0){
        puts("*");
    }

    return 0;
}