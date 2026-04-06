#include <unistd.h>

void ft_putstr(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
    {
        write(1, &str[i], 1);
        i++;
    }
}

int main(int argc, char **argv)
{
    int match;
    int i;
    int j;

    match = 0;
    i = 0;
    j = 0;
    if (argc == 3)
    {
        while (argv[1][i] != '\0')
        {
            while (argv[2][j] != '\0')
            {
                if (argv[1][i] == argv[2][j])
                {
                    match++;
                    j++;
                    break;
                }
                else
                {
                    j++;
                }
            }
        i++;
        }
    }
    if (i == match)
    {
        ft_putstr(argv[1]);
    }
    write(1, "\n", 1);
}
