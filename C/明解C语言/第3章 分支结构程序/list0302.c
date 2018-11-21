/*
    输入的整数是奇数吗？
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个整数：");    scanf("%d", &num);
    if(num % 2){
        puts("输入的整数是奇数。");
    }

    return 0;
}