import random


def main():
    level = get_level()
    numListX = []
    numListY = []
    for i in range(10):
        numListX.append(generate_integer(level))
        numListY.append(generate_integer(level))

    score = 0

    for i in range(10): #for each of 10 levels
        tries = 0
        correct = numListX[i] + numListY[i]
        while tries < 3:
            entered = int(input(f"{numListX[i]} + {numListY[i]} = "))
            if entered == correct:
                score += 1
                break
            else:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{numListX[i]} + {numListY[i]} = {correct}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level and level <= 3:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
