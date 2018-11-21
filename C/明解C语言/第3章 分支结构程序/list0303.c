/*
    输入的整数能被5整除吗？
*/

#include <stdio.h>

int main(void)
{
    int num;

    printf("输入一个整数：");    scanf("%d", &num);
    
    if(num % 5){
        puts("该整数不能被5整除。");
    }
    else{
        puts("该整数能够被5整除。");
    }

    return 0;
}