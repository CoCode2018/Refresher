#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入正整数：");    scanf("%d", &num);

    int bit = 0;
    int temp = num;
    while(temp > 0){
        bit++;
        temp /= 10;
    }

    printf("%d的位数是%d。\n", num, bit);

    return 0;
}