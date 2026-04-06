#include <unistd.h> /* j'inclue le header file */

void    ft_putchar(char c)
{
        write(1, &c, 1);
}
