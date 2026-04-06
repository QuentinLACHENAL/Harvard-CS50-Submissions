import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if re.search(r"60", s):
            raise ValueError
        if re.search(r"[0-9]A|[0-9]P", s):
            raise ValueError
        splitted = s.split("to")
        mins1 = 0
        mins2 = 0
        hours1 = 0
        hours2 = 0

        extracted1 = re.search(r"^([1][0-2]|[1-9]).*", splitted[0]).group(1)

        hours1 += int(extracted1)

        if minutes := re.search(r":([0-5][0-9])", splitted[0]):
            #print(minutes[0][1:3])
            mins1 += int(minutes[0][1:3])
        if re.search("PM", splitted[0]):
            hours1 += 12
        if re.search("12 AM", splitted[0]) or re.search(r"12:.*AM", splitted[0]) or hours1 == 24:
            hours1 = 0
        if re.search("12 PM", splitted[0]):
            hours2 = 12

        #print(extracted1)

        #print(splitted[1])
        extracted2 = re.search(r"([1][0-2]|[1-9]).*?", splitted[1]).group(1)
        #print(extracted2)
        hours2 += int(extracted2)

        if minutes2 := re.search(r":([0-5][0-9])", splitted[1]):
            #print(minutes2[0][1:3])
            mins2 += int(minutes2[0][1:3])
        if re.search("PM", splitted[1]) and not re.search("12", splitted[1]):
            hours2 += 12
        if re.search("12 AM", splitted[1]) or re.search(r"12:.*AM", splitted[1]) or hours2 == 24:
            hours2 = 0
        if re.search("12 PM", splitted[1]):
            hours2 = 12

        return f"{hours1:02d}" + ":" + f"{mins1:02d}" + " to " + f"{hours2:02d}" + ":" + f"{mins2:02d}"
    except:
        raise ValueError


...


if __name__ == "__main__":
    main()
