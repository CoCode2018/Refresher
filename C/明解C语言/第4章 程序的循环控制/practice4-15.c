#include <stdio.h>

int main(void)
{
    int start, end, step;
    printf("开始数值(cm): ");    scanf("%d", &start);
    printf("结束数值(cm): ");    scanf("%d", &end);
    printf("间隔数值(cm): ");    scanf("%d", &step);

    for(; start <= end; start += step){
        printf("%dcm\t%.2fkg\n", start, (start - 70) * 0.6);
    }

    return 0;
}