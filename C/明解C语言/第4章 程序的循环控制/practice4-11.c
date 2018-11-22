#include <stdio.h>

int main(void)
{
    int num;

    do{
        printf("请输入一个正整数：");    
        scanf("%d", &num);
        if(num <= 0){
            puts("请不要输入非负数。");
        }
    }while(num <= 0);

    int temp = num;
    int rev = 0;
    while(temp > 0){
        rev = rev * 10 + temp % 10;
        temp /= 10;
    }
    printf("%d逆向显示的结果是%d.\n", num, rev);

    return 0;
}