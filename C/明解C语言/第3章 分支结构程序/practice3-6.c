#include <stdio.h>

int main(void)
{
    int num1, num2, num3;

    puts("输入3个整数。");
    printf("num1 = ");    scanf("%d", &num1);
    printf("num2 = ");    scanf("%d", &num2);
    printf("num3 = ");    scanf("%d", &num3);

    int min;
    min = num1;
    if(num2 < min)  min = num2;
    if(num3 < min)  min = num3;

    printf("三个整数中的最小值为%d。\n", min);

    return 0;
}