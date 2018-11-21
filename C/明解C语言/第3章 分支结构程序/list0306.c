/*
    输入的两个整数相等吗？
*/

#include <stdio.h>

int main(void)
{
    int num1, num2;

    puts("请输入两个整数。");
    printf("整数1：");    scanf("%d", &num1);
    printf("整数2：");    scanf("%d", &num2);

    if(num1 == num2){
        puts("它们相等。");
    }
    else{
        puts("它们不相等。");
    }

    return 0;
}