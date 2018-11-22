#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个整数: ");    scanf("%d", &num);

    switch(num % 3){
        case 0:    puts("该数能够被3整除。");    break;
        case 1:    puts("该数除以3的余数为1。");    break;
        case 2:    puts("该数除以3的余数为2。");    break;
    }

    return 0;
}