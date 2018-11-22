#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个正整数： ");    scanf("%d", &num);

    int i = 0;
    while(i <= 12){
        // printf("%d ", i);
        printf("%d ", i++);
    }
    printf("\n");

    return 0;
}