#include <stdio.h>

int main(void)
{
    int num;
    int cont = 0;
    int sum = 0;
    printf("输入多少个整数：");    scanf("%d", &cont);

    for(int i = 1; i <= cont; i++){
        printf("No.%d: ", i);
        scanf("%d", &num);
        sum += num;
    }

    printf("合计值：%d\n", sum);
    printf("平均值：%.2f\n", (double)sum / cont);

    return 0;
}