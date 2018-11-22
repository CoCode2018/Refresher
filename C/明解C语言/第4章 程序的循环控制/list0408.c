#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个正整数：");    scanf("%d", &num);

    while(num-- > 0){
        putchar('*');
    }

    return 0;
}