str = input("Input: ")

voyelles = "aeiouAEIOU"

print("Output: ", end="")
for c in str:
    if c not in voyelles:
        print(c, end="")

print("")
