#include <stdio.h>

int main(void)
{
    int num;
    printf("输入一个正整数:  ");   scanf("%d", &num);

    int i = 1;
    if(num >=0){
        while(i <= num){
            printf("%d ", i++);
        }
        printf("\n");
    }

    return 0;
}