/*
*/

#include <stdio.h>

int main(void)
{
    int num1;
    int num2;
    puts("请输入连个整数。");
    printf("整数1: ");    scanf("%d", &num1);
    printf("整数2: ");    scanf("%d", &num2);

    int max;
    max = (num1 >= num2) ? num1 : num2;
    printf("较大的数是%d。\n", max);

    return 0;
}