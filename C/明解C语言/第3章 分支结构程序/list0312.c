/*
    显示所输入的两个整数中较大的数(其二).
*/

#include <stdio.h>

int main(void)
{
    int num1, num2;
    puts("请输入两个整数。");
    printf("整数1： ");    scanf("%d", &num1);
    printf("整数2： ");    scanf("%d", &num2);

    int max;
    if (num1 >= num2)
        max = num1;
    else
        max = num2;
    
    printf("较大的数是%d。\n", max);

    return 0;
}