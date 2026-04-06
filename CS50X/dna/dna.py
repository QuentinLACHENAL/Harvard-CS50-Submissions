import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("ERROR, program needs 3 CLAs. Usage: python script.py <database> <sequence>")
        sys.exit()

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # UNCHECK THIS:
    # for ligne in rows:
        # print(ligne)

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2]) as file2:
        adn_seq = file2.read()

        str_to_check = reader.fieldnames[1:]

    # TODO: Find longest match of each STR in DNA sequence
        str_counts = {}
        for str_seq in str_to_check:
            str_counts[str_seq] = longest_match(adn_seq, str_seq)

    # DEBUG, DEACTIVATE IT BEFORE PUSHING
    # print(longest)
    # print(reader)
    # print(adn_seq)
    # print(rows)

    # TODO: Check database for matching profiles

    # print("STR results DEBUG :", str_counts)

    for profil in rows:
        if all(int(profil[str_]) == str_counts[str_] for str_ in str_to_check):
            print(f"{profil['name']}")
            return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
