#include <stdio.h>

int main(void)
{
    int num;

    do{
        printf("请输入一个正整数:   ");
        scanf("%d", &num);
        if(num <= 0){
            puts("请不要输入非正整数。");
        }
    }while(num <= 0);

    // printf("该整数逆向显示的结果是：");
    // while(num > 0){
    //     printf("%d", num % 10);
    //     num /= 10;
    // }
    // putchar('.');

    int rev = 0;
    while(num > 0){
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    printf("该整数逆向显示的结果是%d.\n", rev);


    return 0;
}