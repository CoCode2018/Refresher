#include <stdio.h>

int main(void)
{
    int retry;
    int sum = 0;
    int times = 0;
    do{
        int num;
        printf("请输入一个整数: ");    scanf("%d", &num);
        times++;
        sum += num;
        printf("是否继续?<Yes...0/No...9>:  ");
        scanf("%d", &retry);
    }while(retry == 0);

    printf("和为%d, 平均值为%.2f\n", sum, (float)sum / times);

    return 0;
}