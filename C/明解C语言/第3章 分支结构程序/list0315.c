/*
    计算输入的两个整数的差并显示(条件运算符)
*/

#include <stdio.h>

int main(void)
{
    int num1, num2;

    puts("请输入两个整数。");
    printf("整数1: ");    scanf("%d", &num1);
    printf("整数2: ");    scanf("%d", &num2);

    printf("它们的差是%d。\n", (num1 > num2) ? (num1 - num2) : (num2 - num1));

    return 0;
}