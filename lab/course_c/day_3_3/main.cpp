#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    int count = 100;

    for (int i = 1; i <= count; i++)
    {
        //версия 1
        // printf("%i", i);
        // i%10 ? printf(" ") : printf("\n");

        //версия 2

        printf("%4i", i);
        if (i%10 == 0) printf("\n");

    }
    

    return 0;
}