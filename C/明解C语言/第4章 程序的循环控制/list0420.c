#include <stdio.h>

int main(void)
{
    int retry;
    int num;
    do{
        
        printf("请输入一个正整数：");    scanf("%d", &num);
        if(num <= 0){
            printf("\a请不要输入非正整数。\n");
        }else{
            for(int i = 1; i <= num; i++){
                putchar('*');
            }
            printf("\n是否继续执行？【Yes...0/No...9】");
            scanf("%d", &retry);
        }
    }while(num <= 0 || retry == 0);

    return 0;
}