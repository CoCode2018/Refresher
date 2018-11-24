#include <stdio.h>

int main(void)
{
    int num;
    puts("让我们来画一个向下的金字塔。");
    printf("金字塔有几层：");    scanf("%d", &num);

    // 一共 2n - 1个字符
    // 每一行*号有： (num - i) * 2 + 1
    int total = 2 * num - 1;

    for(int i = 1; i <= num; i++){
        for(int j = 0; j < (total - (num - i) * 2 + 1)/2; j++){
            putchar(' ');
        }
        for(int j = 1; j <= 2 * (num - i) + 1; j++){
            printf("%d", i % 10);
        }
        for(int j = 0; j < (total - (num - i) * 2 + 1)/2; j++){
            putchar(' ');
        }
        putchar('\n');
    }

    return 0;
}