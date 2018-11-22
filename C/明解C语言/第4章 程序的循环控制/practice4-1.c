#include <stdio.h>

int main(void)
{
    int retry;

    do{
        int num;
        printf("输入要判断符号的数值:  ");
        scanf("%d", &num);
        if(num == 0){
            puts("该数值为0.");
        }
        else if(num < 0){
            puts("该数值为负数。");
        }
        else{
            puts("该数值为正数。");
        }
        printf("是否要继续【Yes...0/No...9】:  ");
        scanf("%d", &retry);
    }while(retry == 0);

    return 0;
}