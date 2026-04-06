import sys

nameList = []

while True:
    try:
        name = input("Name: ")
        nameList.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to ", end="")
        if len(nameList) == 1:
            print(nameList[0])
        elif len(nameList) > 1:
            i = 0
            while i < len(nameList) - 1:
                print(f"{nameList[i]}", end="")
                i += 1
                if len(nameList) != 2:
                    print(", ", end="")
                else:
                    print(" ", end="")
            print(f"and {nameList[i]}", end="")
            print()
        sys.exit()
