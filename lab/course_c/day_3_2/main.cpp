#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int a,b,c,max=0;

    printf("Input a b c:");
    scanf("%i %i %i", &a, &b, &c);
    printf("a=%d b=%d c=%d\n", a, b, c);


    // Способ 1

    // max = a>b?a:b;

    // if (c > max){
    //     max = c;
    // }

    // Способ 2

    max = (a>b) ? (a>c)?a:c  :  (b>c)?b:c;

    // Вариант 2 не читабельный
    // max = a>b?a>c?a:c:b>c?b:c;



    printf("max=%d\n",max);
    return 0;
}