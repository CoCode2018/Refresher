#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个正整数:  ");   scanf("%d", &num);

    int i = 2;
    while(i <= num){
        printf("%d ", i);
        i += 2;
    }

    return 0;
}