/*
    读取两个整数，显示它们的商和余数
*/

#include <stdio.h>

int main(void)
{
    int a, b;
    puts("输入两个整数：");
    printf("整数a = ");    scanf("%d", &a);
    printf("整数b = ");    scanf("%d", &b);

    printf("a除以b得 %d余 %d。\n", a / b, a % b);

    return 0;
}