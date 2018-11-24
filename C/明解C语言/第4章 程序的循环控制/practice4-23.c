#include <stdio.h>

int main(void)
{
    int num;
    printf("输入短边：");    scanf("%d", &num);

    puts("直角在左上方：");
    for(int i = num; i > 0; i--){
        for(int j = i; j > 0; j--){
            putchar('*');
        }
        putchar('\n');
    }

    putchar('\n');
    puts("直角在右上方：");
    for(int i = num; i > 0; i--){
        for(int j = 0; j < num - i; j++){
            putchar(' ');
        }
        for(int j = i; j > 0; j--){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}
