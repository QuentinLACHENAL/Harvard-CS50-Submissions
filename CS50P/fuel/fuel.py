while True:
    fract = input("Fraction: ")

    try:
        slashPos = fract.find("/")
        preSlash = fract[:slashPos]
        postSlash = fract[slashPos + 1:]
        if (not preSlash.isdigit() or not postSlash.isdigit()):
            raise ValueError
    except:
        continue

    x = int(preSlash)
    y = int(postSlash)

    try:
        if y == 0:
            raise ZeroDivisionError
    except:
        continue

    result = x / y * 100

    if result > 100:
        continue

    if result >= 99:
        print("F")
        break
    elif result <= 1:
        print("E")
        break
    else:
        print(f"{result:.0f}%")
        break
