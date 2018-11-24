#include <stdio.h>

int main(void)
{
    puts("不包含4的九九法则：");

    for(int i = 1; i <= 9; i++){
        for(int j = 1; j <= 9; j++){
            int ji = i * j;
            // if(ji % 10 != 4){
            //     printf("%3d", ji);
            // }
            // else if(ji / 10 != 4){
            //     printf("%3d", ji);
            // }
            // else{
            //     printf("%3c", ' ');
            //     continue;
            // }
            if(ji % 10 == 4 || ji % 10 == 4){
                printf("%3c", ' ');
                continue;
            }
            printf("%3d", ji);
        }
        putchar('\n');
    }
    return 0;
}