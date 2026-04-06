#include <unistd.h>

void    print_a(void)
{
    char    letter;

    letter = 'a';
    write(1, &letter, 1);
}

int main(void)
{
    print_a();
    return (0);
}
