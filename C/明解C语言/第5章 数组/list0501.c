#include <stdio.h>

int main(void)
{
    int x1,x2,x3,x4,x5;
    int sum = 0;
    puts("请输入5名学生的分数。");
    printf("1号：");    scanf("%d", &x1);   sum += x1;
    printf("2号：");    scanf("%d", &x2);   sum += x2;
    printf("3号：");    scanf("%d", &x3);   sum += x3;
    printf("4号：");    scanf("%d", &x4);   sum += x4;
    printf("5号：");    scanf("%d", &x5);   sum += x5;

    printf("总分：%5d\n", sum);
    printf("平均分：%5.1f\n", (double)sum / 5);

    return 0;
    
}