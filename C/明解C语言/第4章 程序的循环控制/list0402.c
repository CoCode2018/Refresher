#include <stdio.h>

int main(void)
{
    int hand;

    do{
        printf("请选择出什么拳【0...石头/1...剪刀/2...布】:  ");    
        scanf("%d", &hand);
    }while(hand > 2 || hand < 0);
    switch(hand){
        case 0:    puts("你选择了石头。");    break;
        case 1:    puts("你选择了剪刀。");    break;
        case 2:    puts("你选择了布。");     break;
    }

    return 0;
}