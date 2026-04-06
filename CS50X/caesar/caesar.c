#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(char *str)
{
    int i;

    i = 0;
    while (str[i] != '\0')
    {
        if ('0' <= str[i] && str[i] <= '9')
            i++;
        else
        {
            printf("Usage: ./caesar key");
            return 0;
        }
    }
    return 1;
}

int main(int argc, char **argv)
{
    int i;
    int k;
    char *plaintext;
    int size;

    size = 1000;
    plaintext = malloc(size * sizeof(char));
    if (plaintext == NULL)
    {
        printf("memory allocation error");
        return (1);
    }
    // if there is not 1 CLA, print error message and return 1
    if (argc != 2)
    {
        printf("Error, CLA != 1. Usage: ./caesar key\n");
        return (1);
    }
    // if CLA isn't made of digits, return 1 and usage
    if (only_digits(argv[1]) == 0)
        return (1);
    // k must be 2^31 - 26 and non negative
    k = atoi(argv[1]);
    if (k < 0 || 2147483622 < k)
    {
        printf("key must be between 0 and 2147483622");
        return (1);
    }
    // must preserve case
    // must output "plaintext: "
    printf("plaintext: ");
    fgets(plaintext, size, stdin);
    plaintext[strcspn(plaintext, "\n")] = '\0';
    i = 0;
    printf("ciphertext: ");
    while (plaintext[i] != '\0')
    {
        if ('a' <= plaintext[i] && plaintext[i] <= 'z')
        {
            plaintext[i] = (plaintext[i] + k - 'a') % 26 + 'a';
            printf("%c", plaintext[i]);
            i++;
        }
        else if ('A' <= plaintext[i] && plaintext[i] <= 'Z')
        {
            plaintext[i] = (plaintext[i] + k - 'A') % 26 + 'A';
            printf("%c", plaintext[i]);
            i++;
        }
        else
        {
            printf("%c", plaintext[i]);
            i++;
        }
    }
    printf("\n");
    free(plaintext);
    return (0);
    // must output "ciphertext: "

    // print a newline
}
