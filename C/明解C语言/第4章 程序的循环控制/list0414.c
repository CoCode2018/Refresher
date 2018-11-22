#include <stdio.h>

int main(void)
{
    int num;
    printf("整数值： ");    scanf("%d", &num);

    for(int i = 2; i <= num; i += 2){
        printf("%d ", i);
    }

    return 0;
}