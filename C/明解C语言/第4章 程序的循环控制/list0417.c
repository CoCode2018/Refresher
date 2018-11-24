#include <stdio.h>

int main(void)
{
    int height, width;
    printf("高：");    scanf("%d", &height);
    printf("宽：");    scanf("%d", &width);

    for(int i = 1; i <= height; i++){
        for(int j = 1; j <= width; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}