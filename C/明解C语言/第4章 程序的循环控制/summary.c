#include <stdio.h>

int main(void)
{
    int num;
    do{
        printf("0~100的整数值：");
        scanf("%d", &num);
    }while(num < 0 || num > 100);

    int add = num;
    int sub = num;

    while(sub > 0 ){
        printf("%d    %d\n", sub--, ++add);
    }
    printf("宽和高位整数面积为%d的长方形的边长是：\n", num);
    for(int i = 1; i < num; i++){
        if(i * i > num)    break;
        if(num % i != 0) continue;
        printf("%d x %d\n", i, num / i);
    }

    puts("5行7列的星号");
    for(int i = 1; i <= 5; i++){
        for(int j = 1; j <= 7; j++){
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}