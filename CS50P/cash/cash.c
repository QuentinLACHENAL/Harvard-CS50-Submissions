#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int change_owed = 0;

    do
    {
        change_owed = get_int("How many coins should I give back?\n");
    }
    while (change_owed < 1);

    int number_of_quarters = 0;
    int number_of_dimes = 0;
    int number_of_nickels = 0;
    int number_of_pennies = 0;

    while (change_owed >= 25)
    {

        change_owed -= 25;
        number_of_quarters++;
    }
    while (change_owed >= 10)
    {

        change_owed -= 10;
        number_of_dimes++;
    }
    while (change_owed >= 5)
    {

        change_owed -= 5;
        number_of_nickels++;
    }
    while (change_owed >= 1)
    {

        change_owed -= 1;
        number_of_pennies++;
    }

    printf("%i\n", number_of_quarters + number_of_pennies + number_of_nickels + number_of_dimes);
}
