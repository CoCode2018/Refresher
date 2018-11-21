#include <stdio.h>

int main(void)
{
    int num1, num2, num3;
    puts("输入3个整数。");
    printf("Num1 = ");    scanf("%d", &num1);
    printf("Num2 = ");    scanf("%d", &num2);
    printf("Num3 = ");    scanf("%d", &num3);

    int min = num1;
    min = min < ((num2 < num3) ? num2 : num3) ? min : ((num2 < num3) ? num2 : num3);
    printf("三个数中最小的是%d。\n", min);

    return 0;
}