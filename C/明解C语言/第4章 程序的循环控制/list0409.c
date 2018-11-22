#include <stdio.h>

int main(void)
{
    int index = 0;
    int sum = 0;
    int num;
    int temp;

    printf("要输入多少个整数:  ");    scanf("%d", &num);
    if(num > 0){
        do{
            printf("No.%d = ", ++index);
            scanf("%d", &temp);
            sum += temp;
        }while(index < num);
    }
    printf("合计值:  %d\n", sum);
    printf("平均值:  %.2f\n", (double)sum / num);

    return 0;
}