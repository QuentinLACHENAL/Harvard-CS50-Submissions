def main():
    while True:
        fract = input("Fraction: ")
        result = convert(fract)
        gaugeVal = gauge(result)

        print(f"{gaugeVal}")
        break

def convert(fract):
    #try:
    slashPos = fract.find("/")
    preSlash = fract[:slashPos]
    postSlash = fract[slashPos + 1:]
    if (not preSlash.isdigit() or not postSlash.isdigit()):
        raise ValueError
    #except:
    #    continue

    x = int(preSlash)
    y = int(postSlash)

    #try:
    if y == 0:
        raise ZeroDivisionError
    if x < 0:
        raise ValueError;
    if y < 0:
        raise ValueError;
    #except:
    #    continue

    result = x / y * 100

    return result

def gauge(percentage):
    if percentage >= 99:
        return "F"

    elif percentage <= 1:
        return "E"

    return f"{round(percentage)}%"

if __name__ == "__main__":
    main()
