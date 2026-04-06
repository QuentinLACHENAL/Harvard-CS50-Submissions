#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pyramid_height;

    pyramid_height = 0;

    while (pyramid_height < 1)
    {
        pyramid_height = get_int("Specify how high is the pyramid:");
    }

    int n;
    int spaces;
    int hashes;

    n = 1;

    while (n <= pyramid_height)
    {

        spaces = pyramid_height - n;
        hashes = n;

        while (spaces > 0)
        {
            printf(" ");
            spaces--;
        }

        while (hashes > 0)
        {
            printf("#");
            hashes--;
        }
        n++;
        printf("\n");
    }
    printf("\n");
    return 0;
}
