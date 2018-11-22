#include <stdio.h>

int main(void)
{
    int num;
    printf("请输入一个正整数： ");    scanf("%d", &num);

    if(num >=0){
        while(num >= 0){
            printf("%d ", num);
            num--;
        }
        putchar('\n');
    }

    return 0;
}