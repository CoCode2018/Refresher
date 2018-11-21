#include <stdio.h>

int main(void)
{
    int num1, num2, num3;
    puts("输入三个整数。");
    printf("整数A: ");    scanf("%d", &num1);
    printf("整数B: ");    scanf("%d", &num2);
    printf("整数C: ");    scanf("%d", &num3);

    if(num1 == num2 && num2 == num3){
        puts("三个值都相等。");
    }
    else if(num1 == num2 || num1 == num3 || num2 == num3){
        puts("有两个值相等。");
    }
    else{
        puts("三个值各不相等。");
    }

    return 0;
}