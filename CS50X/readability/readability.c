#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    // index = 0.0588 * L - 0.296 * S - 15.8
    int L;
    float S;
    L = (letters / (float) words) * 100;
    S = (sentences / (float) words) * 100;

    int index;
    index = round((0.0588 * L) - (0.296 * S) - 15.8);

    // Print the grade level
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    if (index >= 1 && index < 16)
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    // Return the number of letters in text
    int letters;
    int i;

    letters = 0;
    i = 0;
    while (text[i] != '\0')
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            letters++;
        }
        i++;
    }
    return (letters);
}

int count_words(string text)
{
    // Return the number of words in text
    int words;
    int i;

    words = 1;
    i = 0;
    while (text[i] != '\0')
    {
        if (text[i] == ' ')
        {
            words++;
        }
        i++;
    }
    return (words);
}

int count_sentences(string text)
{
    // Return the number of sentences in text
    int sentences;
    int i;

    sentences = 0;
    i = 0;
    while (text[i] != '\0')
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        i++;
    }
    return (sentences);
}
