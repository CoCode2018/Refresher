#include <stdio.h>

int main(void)
{
    int x, y;

    puts("请输入两个整数。");
    printf("整数x: ");    scanf("%d", &x);
    printf("整数y: ");    scanf("%d", &y);

    // printf("x的值是y的%d%%.\n", ( 10 * x/y + x%y/y/10) * 10);
    printf("x的值是y的%.0f%%.\n", (x * 1.0 / y) * 100);

    return 0;
}