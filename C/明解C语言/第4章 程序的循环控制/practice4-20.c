#include <stdio.h>

int main(void)
{
    for(int i = -1; i <= 9; i++){
        for(int j = -1; j <= 9; j++){
            if(i == -1 && j == -1){
                printf("%3c", ' ');
            }
            else if(i == -1 && j == 0){
                printf("%3c", '|');
            }
            else if(i == -1 && j != -1 && j != 0){
                printf("%3d", j);
            }
                        else if(i == 0){
                printf("%3c", '-');
            }
            else if(i != -1 && i != 0 && j == -1){
                printf("%3d", i);
            }
            else if(i != -1 && i != 0 && j == 0){
                printf("%3c", '|');
            }
            else{
                printf("%3d", j * i);
            }
        }
        putchar('\n');
    }

    return 0;
}