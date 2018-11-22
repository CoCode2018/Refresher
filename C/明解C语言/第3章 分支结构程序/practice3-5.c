/*
    编写一段程序，确认相等运算符和关系运算符的结果是1和0
*/

#include <stdio.h>

int main(void)
{
    printf("(1 > 2) = %d\n", 1 > 2);
    printf("(1 == 2) = %d\n", 1 == 2);
    printf("(1 == 1) = %d\n", 1 == 1);

    return 0;
}