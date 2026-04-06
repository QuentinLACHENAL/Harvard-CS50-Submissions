import pyfiglet
import sys
from pyfiglet import Figlet

figlet = Figlet()

if (len(sys.argv)) == 1:

    str = input("Input: ")
    str = pyfiglet.figlet_format(str, font="slant")

    print(str)

elif (len(sys.argv)) == 3:

    fontList = figlet.getFonts()

    usedFont = sys.argv[2]
    if not usedFont in fontList:
        print("no")
        exit("Invalid usage")

    if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        str = input("Input: ")
        try:
            str = pyfiglet.figlet_format(str, font=usedFont)
            print(str)
        except:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Need 0 or 2 arguments")
