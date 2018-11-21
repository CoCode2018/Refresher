/*
    输入的整数值是奇数还是偶数。
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个整数：");    scanf("%d", &num);

    if(num % 2){
        puts("该数为奇数。");
    }
    else{
        puts("该数为偶数。");
    }

    return 0;
}