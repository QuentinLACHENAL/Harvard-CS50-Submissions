import sys

def main():
    args = len(sys.argv)
    count = 0
    if args < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif args > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    fileName = sys.argv[1]
    extension = ""
    if fileName.rfind("."):
        extension = fileName[fileName.rfind("."):]
    if extension != ".py":
        print("Not a Python file")
        sys.exit(1)
    try:
        with open(fileName, "r") as file:
            for line in file:
                strippedLine = line.strip()
                if strippedLine[0:1] == '#' or strippedLine == "":
                    continue
                else:
                    count += 1
        print(count)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
