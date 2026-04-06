#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Iterate over each candidate
    int i;

    i = 0;
    while (i < candidate_count)
    {
        // Check if candidate's name matches given name
        if (strcmp(name, candidates[i].name) == 0)
        {
            // If yes, increment candidate's votes and return true
            candidates[i].votes++;
            return true;
        }
        i++;
    }
    // If no match, return false
    return false;
}

void swap_strings(char **str1, char **str2)
{
    char *temp = *str1;
    *str1 = *str2;
    *str2 = temp;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int i;
    int j;

    i = 0;
    while (i < candidate_count - 1)
    {
        j = i + 1;
        while (j < candidate_count)
        {
            if (candidates[i].votes < candidates[j].votes)
            {
                swap_strings(&candidates[i].name, &candidates[j].name);
            }
            j++;
        }
        i++;
    }

    // ajouter    if (candidate[i].votes == candidate[i + j].votes)
    //    {

    //    }

    printf("%s\n", candidates[0].name);
    i = 0;
    while (candidates[i].votes == candidates[i + 1].votes)
    {
        printf("%s\n", candidates[i + 1].name);
        i++;
    }

    return;
}
