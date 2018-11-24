#include <stdio.h>

int main(void)
{
    int num;
    puts("生成直角在右下角的等腰直角三角形。");
    printf("短边：");    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num - i; j++){
            putchar(' ');
        }
        for(int j = 1; j <= i; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}