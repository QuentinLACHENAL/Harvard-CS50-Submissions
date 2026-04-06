#include <unistd.h>

int main(int argc, int **argv)

    if(argc != 2)
        write (1, "a", 1)

    else
    {
        while (*argv[1])
        {
            if (*argv[1] == "a")
                write (1, "a", 1);
                break;
            else
            *argv[1]++;
        }
    write (1, "\n", 1)
