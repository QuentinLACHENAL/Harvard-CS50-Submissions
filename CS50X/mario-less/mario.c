#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pyramid_height;

    // Demander une hauteur valide
    pyramid_height = 0;
    while (pyramid_height < 1)
    {
        pyramid_height = get_int("Specify how high is the pyramid: ");
    }

    int n = 1; // Variable pour suivre la ligne actuelle

    // Construire la pyramide
    while (n <= pyramid_height)
    {
        int spaces = pyramid_height - n; // Espaces nécessaires pour aligner à droite
        int hashes = n;                  // Nombre de # à imprimer

        // Imprimer les espaces
        while (spaces > 0)
        {
            printf(" ");
            spaces--;
        }

        // Imprimer les #
        while (hashes > 0)
        {
            printf("#");
            hashes--;
        }

        printf("\n"); // Passer à la ligne suivante
        n++;          // Incrémenter la ligne actuelle
    }

    return 0;
}
