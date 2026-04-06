// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 19683;
// 26*26*26 = 17576 (so 0 - 17575)

// Hash table
node *table[N];

// I add word count???
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *trav = table[hash(word)];
    while (trav != NULL)
    {
        if (strcasecmp(word, trav->word) == 0)
            return true;
        trav = trav->next;
    }
    //
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    int key = 0;
    if (strlen(word) > 2)
    {
        key = (toupper(word[0]) - 'A' + 1) * (toupper(word[1]) - 'A' + 1) *
              (toupper(word[2]) - 'A' + 1);
    }
    else if (strlen(word) > 1)
    {
        key = (toupper(word[0]) - 'A' + 1) * (toupper(word[1]) - 'A' + 1);
    }
    else
    {
        key = toupper(word[0]) - 'A';
    }
    if (key < 0)
        return 0;
    return key;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
        return (false);
    // Read each word in the file

    char word[50];

    while ((fscanf(source, "%s", word)) ==
           1) // ERREUR IMPORTANTE: OUBLI DES " " AUTOURS DU "%s" sinon ce n'est pas une chaine
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            free(n);
            return false;
        }
        strcpy(n->word, word);
        word_count++;
        // Add each word to the hash table
        n->next = table[hash(word)];
        table[hash(word)] = n;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return (word_count);
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int i = 0;
    node *tmp;
    while (i < N)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
        i++;
    }
    //
    return true;
}
