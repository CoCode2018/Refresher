#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个正整数:  ");    scanf("%d", &num);

    while(num >= 0){
        printf("%d ", num--);
    }

    return 0;
}