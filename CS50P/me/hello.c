#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name;
    name = get_string("What's your name?\n");
    printf("hello, %s\n", name);
}
