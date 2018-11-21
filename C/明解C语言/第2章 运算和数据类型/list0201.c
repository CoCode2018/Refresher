/*
    读取两个整数的值，然后显示出它们的和差积商和余数
*/

#include <stdio.h>

int main(void)
{
    int x1, x2;

    puts("输入两个整数。");
    printf("x1 = ");    scanf("%d", &x1);
    printf("x2 = ");    scanf("%d", &x2);

    printf("x1 + x2 = %d\n", x1 + x2);
    printf("x1 - x2 = %d\n", x1 - x2);
    printf("x1 * x2 = %d\n", x1 * x2);
    printf("x1 / x2 = %d\n", x1 / x2);
    printf("x1 %% x2 = %d\n", x1 % x2);

    return 0;
}