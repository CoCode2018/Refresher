#include <stdio.h>

int main(void)
{
    int num1, num2, sub;
    puts("输入两个整数。");
    printf("num1= ");    scanf("%d", &num1);
    printf("num2= ");    scanf("%d", &num2);

    sub = (num1 > num2) ? (num1 - num2) : (num2 - num1);

    if(sub <= 10)
        puts("它们的差小于等于10。");
    else{
        puts("它们的差大于等于11。");
    }
    return 0;
}