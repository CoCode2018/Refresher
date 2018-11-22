#include <stdio.h>

int main(void)
{
    int num;
    printf("整数值： ");    scanf("%d", &num);

    for(int i = 1; i <= num; i++){
        if(num % i == 0){
            printf("%d ", i);
        }
    }

    return 0;
}