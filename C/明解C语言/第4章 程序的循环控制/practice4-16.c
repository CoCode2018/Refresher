#include <stdio.h>

int main(void)
{
    int num;
    printf("整数值: ");    scanf("%d", &num);

    // for(int i = 1; i <= num; i += 2){
    //     printf("%d ", i);
    // }
    int i = 1;
    while(i <= num){
        if(i % 2){
            printf("%d ", i++);
        }
        else{
            i++;
        }
    }

    return 0;
}