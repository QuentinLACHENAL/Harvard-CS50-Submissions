#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Saisie des mots pour les deux joueurs
    string p1_word = get_string("Player 1: ");
    string p2_word = get_string("Player 2: ");

    int p1_score = 0;
    int p2_score = 0;

    // Points associés à chaque lettre
    int letter_points[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                             1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // Calcul du score pour Player 1
    int i = 0;
    while (p1_word[i] != '\0')
    {
        if (isalpha(p1_word[i])) // Vérifie si le caractère est alphabétique
        {
            int index = tolower(p1_word[i]) - 'a'; // Convertit la lettre en index alphabétique
            p1_score += letter_points[index];
        }
        i++;
    }

    // Calcul du score pour Player 2
    i = 0; // Réinitialise i pour la seconde boucle
    while (p2_word[i] != '\0')
    {
        if (isalpha(p2_word[i])) // Vérifie si le caractère est alphabétique
        {
            int index = tolower(p2_word[i]) - 'a';
            p2_score += letter_points[index];
        }
        i++;
    }

    // Déterminer le gagnant
    printf("\n");
    if (p1_score > p2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (p1_score < p2_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}
