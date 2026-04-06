import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        if re.match(r"^<iframe.*src=\".*\".*></iframe>", s):
            extracted = re.search(r"src=\"http(?:s)?://(?:www\.)?youtube\.com/embed/(.*?)\"", s).group(1)
            return "https://youtu.be/" + extracted #modified str
        else:
            return None
    except AttributeError:
        return None


...


if __name__ == "__main__":
    main()
