/*
    判断后者是否为前者的约数
*/

#include <stdio.h>

int main(void)
{
    int num1, num2;
    puts("输入两个整数。");
    printf("整数A：");    scanf("%d", &num1);
    printf("整数B：");    scanf("%d", &num2);

    if(num1 / num2){
        puts("B不是A的约数。");
    }
    else{
        puts("B是A的约数。");
    }

    return 0;
}