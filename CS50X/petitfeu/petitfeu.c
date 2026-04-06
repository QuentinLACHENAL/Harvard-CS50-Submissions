#include <cs50.h>
#include <stdio.h>

int main    (void)
{
    int pyramid_height;


    pyramid_height = 0;


    while (pyramid_height < 1)
    {
        pyramid_height = get_int("Specify how high is the pyramid:");
    }

    int n;
    int spaces;
    int hashs;

    n = 1;

    while (pyramid_height > 0)
    {


        spaces = (pyramid_height - n);
        hashs = (n);

        while (spaces > 0)
        {
        printf(" ");
        spaces --;
        }

        while (hashs > 0)
        {
        printf("#");
        hashs --;
        }
        pyramid_height--;
        n++;
        printf("\n");

    }
    printf("\n");
}
