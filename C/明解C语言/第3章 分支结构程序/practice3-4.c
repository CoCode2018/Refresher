#include <stdio.h>

int main(void)
{
    int num1, num2;
    puts("请输入两个整数。");
    printf("整数A: ");    scanf("%d", &num1);
    printf("整数B: ");    scanf("%d", &num2);

    if(num1 == num2){
        printf("A和B相等。\n");
    }
    else if(num1 > num2){
        printf("A大于B。\n");
    }
    else{
        printf("A小于B。\n");
    }

    return 0;
}