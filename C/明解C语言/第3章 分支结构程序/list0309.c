/*
    判断输入整数的符号。
*/

#include <stdio.h>

int main(void)
{
    int num;

    printf("输入一个整数：");    scanf("%d", &num);
    
    if(num == 0){
        puts("该整数位0。");
    }
    else if(num > 0){
        puts("该整数为整数。");
    }
    else{
        puts("该整数为负数。");
    }

    return 0; 
}
