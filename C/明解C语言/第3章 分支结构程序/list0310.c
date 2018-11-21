/*
    如果输入的整数值为正，则判断该值的奇偶性并显示。
*/

#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个整数： ");    scanf("%d", &num);

    if(num > 0){
        if(num % 2){
            printf("该整数为奇数。\n");
        }
        else{
            printf("该整数为偶数。\n");
        }
    }
    else{
        puts("您输入的不是正数\a\a\a");
    }

    return 0;
}
