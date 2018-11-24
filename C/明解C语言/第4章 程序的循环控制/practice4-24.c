#include <stdio.h>

int main(void)
{
    int num;
    printf("金字塔的层数：");    scanf("%d", &num);

    // n层的金字塔每一层包含：2n-1个字符 
    // 每一层*号有：(n-1) * 2 + 1
    // 每一层 号有：

    int total = 2 * num - 1;

    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= (total - (i-1)*2+1)/2; j++){
            putchar(' ');
        }
        for(int j = 1; j <= (i-1)*2+1; j++){
            putchar('*');
        }
                for(int j = 1; j <= (total - (i-1)*2+1)/2; j++){
            putchar(' ');
        }
        putchar('\n');
    }

    return 0;
}