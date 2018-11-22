/*
    计算所输入的三个整数中的最大值并显示
*/

#include <stdio.h>

int main(void)
{
    int num1, num2, num3;
    puts("请输入三个整数。");
    printf("整数1： ");    scanf("%d", &num1);
    printf("整数2： ");    scanf("%d", &num2);
    printf("整数3： ");    scanf("%d", &num3);

    int max;
    max = num1;
    if(num2 > max)
        max = num2;
    if(num3 > max)
        max = num3;
    
    printf("最大值是%d。\n", max);

    return 0;

}