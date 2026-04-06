def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print(f"${val}")


def value(greeting):
    greeting = greeting[:5].upper().strip()
    if greeting == "HELLO":
        return 0
    elif greeting[0:1] == 'H':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
