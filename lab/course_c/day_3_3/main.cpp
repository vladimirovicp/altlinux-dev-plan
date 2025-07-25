#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    int count = 100;

    for (int i = 1; i <= count; i++)
    {
        printf("%i", i);
        
        i%10 ? printf(" ") : printf("\n");
    }
    

    return 0;
}