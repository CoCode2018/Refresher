#include <stdio.h>

int main(void)
{
    for(int i = 1; i <= 9; i++){
        for(int j = 1; j <= 9; j++){
            if(i * j > 40){
                break;
            }
            else{
                printf(" %3d ", i * j);
            }
            
        }
        putchar('\n');
    }

    return 0;
}