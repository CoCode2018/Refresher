#include <stdio.h>

int main(void)
{
    int num;
    puts("生成一个正方形");
    printf("正方形有几层：");    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}