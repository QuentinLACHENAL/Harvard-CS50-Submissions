word = input("camelCase: ")

print("snake_case: ", end="")

for c in word:
    if c.isupper():
        print("_", end="")
        c = c.lower()
    print(c, end="")

print("")

