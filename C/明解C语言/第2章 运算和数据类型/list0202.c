/*
    显示读取出的整数的最后一位数字
*/

#include <stdio.h>

int main(void)
{
    int no;
    printf("输入一个整数：");    scanf("%d", &no);

    printf("最后一位数字为%d.\n", no % 10);

    printf("no = %d\n", no);
    // 整数部分 + 余数部分 == 原来的数
    printf("(x/y)*y + x %% y = %d\n", (no / 2) * 2 + no % 2);

    return 0;
}