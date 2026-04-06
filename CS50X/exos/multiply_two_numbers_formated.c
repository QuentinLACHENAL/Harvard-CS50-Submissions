#include <stdio.h>
#include <stdlib.h>

float multiply_two_reals(float x, float y)
{
    return x * y;
}

int main(int argc, char **argv)
{
    float x;    //declare//
    float y;
    float z;

    if  (argc != 3)
    {
        printf("Usage: ./test x y\n");
        return 1;
    }

    x = strtof(argv[1], NULL);  //initialize//
    y = strtof(argv[2], NULL);

    z = multiply_two_reals(x, y);   //calculate//
    printf("%f\n", z);

    return 0;
}
