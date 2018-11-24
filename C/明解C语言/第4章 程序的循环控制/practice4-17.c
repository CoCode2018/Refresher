#include <stdio.h>

int main(void)
{
    int num;
    printf("n的值：");    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        printf("%d的二次方是%d\n", i, i*i);
    }

    return 0;
}