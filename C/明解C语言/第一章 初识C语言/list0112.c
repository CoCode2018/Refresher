/*
    读取一个整数并显示其5倍数的值
*/

#include <stdio.h>

int main(void)
{
    int no;

    printf("请输入一个整数值: ");
    scanf("%d", &no);

    printf("它的5倍数是%d.\n", no * 5);

    return 0;
}