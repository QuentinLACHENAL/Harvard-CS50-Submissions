#include <stdio.h>
#include <stdlib.h>

float   multiply_two_reals(float x, float y)
{
    return x * y;
}

int    main(int argc, char **argv)
{
    if  (argc != 3)
    {
        printf("Usage: ./test x y\n");
        return 1;
    }
    else
    {
        float x = strtof(argv[1], NULL);
        float y = strtof(argv[2], NULL);

        float z = multiply_two_reals(x, y);
        printf("%f\n", z);
        return 0;
    }
}
