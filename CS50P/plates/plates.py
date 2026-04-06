def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

forbidden = " .!?"
flag = False

def is_valid(s):

    if 2 > len(s) or len(s) > 6:
        return 0
    if not s[0].isalpha() or not s[1].isalpha():
        return 0
    for c in s:
        global flag
        if c.isdigit():
            if flag == False:
                if c == "0":
                    return 0
            flag = True
        if flag == True:
            if c.isalpha():
                return 0
    for c in s:
        if c in forbidden:
            return 0

    return 1


main()
