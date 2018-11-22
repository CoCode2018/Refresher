#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个正整数：");    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        putchar('*');
    }

    return 0;
}