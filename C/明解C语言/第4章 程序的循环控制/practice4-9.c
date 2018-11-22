#include <stdio.h>

int main(void)
{
    int num;
    printf("正整数： ");    scanf("%d", &num);

    int i = 1;

    while(i++ <= num){
        if(i % 2){
            putchar('-');
        }
        else{
            putchar('+');
        }
    }

    return 0;
}