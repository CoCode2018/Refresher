#include <stdio.h>

int main(void)
{
    int num1, num2;
    puts("让我们来画一个长方形。");
    printf("一边：");    scanf("%d", &num1);
    printf("另一边：");  scanf("%d", &num2);

    int max = (num1 > num2) ? num1 : num2;
    int min = (num1 < num2) ? num1 : num2;

    for(int i = 1; i <= min; i++){
        for(int j = 1; j <= max; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}