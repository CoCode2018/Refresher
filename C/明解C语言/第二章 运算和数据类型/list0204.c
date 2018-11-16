/*
    对读取的整数值进行符号取反操作
*/

#include <stdio.h>

int main(void)
{
    int num;

    printf("请输入一个整数: ");
    scanf("%d", &num);

    printf("符号取反之后的值是%d.\n", -num);

    return 0;
}