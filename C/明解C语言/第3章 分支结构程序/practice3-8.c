#include <stdio.h>

int main(void)
{
    int num1, num2;
    puts("请输入两个整数。");

    printf("整数1: ");    scanf("%d", &num1);
    printf("整数2: ");    scanf("%d", &num2);

    int sub;
    if(num1 > num2)    sub = num1 - num2; else sub = num2 - num1;
    
    printf("它们的差是%d。\n", sub);

    return 0;

}