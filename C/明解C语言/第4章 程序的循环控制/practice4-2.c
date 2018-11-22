#include <stdio.h>

int main(void)
{
    int num1;
    int num2;

    puts("请输入两个整数。");
    printf("整数a: ");    scanf("%d", &num1);
    printf("整数b: ");    scanf("%d", &num2);

    int max, min, temp;

    max = (num1 >= num2) ? num1 : num2;
    min = (num1 < num2) ? num1 : num2;
    temp = min;

    int sum = 0;
    do{
        sum += temp;
        temp++;
    }while(temp <= max);

    printf("大于等于%d小于等于%d的所有整数的和是%d。\n", min, max, sum);

    return 0;
}