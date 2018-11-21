#include <stdio.h>

int main(void)
{
    int num1, num2, num3, num4;

    puts("输入四个整数。");
    printf("num1 = ");    scanf("%d", &num1);
    printf("num2 = ");    scanf("%d", &num2);
    printf("num3 = ");    scanf("%d", &num3);
    printf("num4 = ");    scanf("%d", &num4);

    int max;
    max = ((num1 > num2) ? num1 : num2) > ((num3 > num4) ? num3 : num4) ?
        ((num1 > num2) ? num1 : num2) : ((num3 > num4) ? num3 : num4);
    
    printf("最大值为%d。\n", max);

    return 0;

}