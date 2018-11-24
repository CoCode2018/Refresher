#include <stdio.h>

int main(void)
{
    int len;
    puts("生成直角在左下方的等腰直角三角形。");

    printf("短边：");    scanf("%d", &len);
    for(int i = 1; i <= len; i++){
        for(int j = 1; j <= i; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}