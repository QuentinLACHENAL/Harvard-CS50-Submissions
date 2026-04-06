def main():
    word = input("Input: ")
    word = shorten(word)
    print(f"Output: {word}")


def shorten(word):
    voyelles = "aeiouAEIOU"
    newWord = ""
    for c in word:
        if c not in voyelles:
            newWord = newWord + c
    return newWord


if __name__ == "__main__":
    main()
