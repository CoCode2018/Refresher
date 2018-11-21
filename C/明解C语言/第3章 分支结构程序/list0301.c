/*
    输入的整数能被5整除吗？
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个整数：");    scanf("%d", &num);

    if(num % 5){
        puts("输入的整数不能被5整除。");
    }
}