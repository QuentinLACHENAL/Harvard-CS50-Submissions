import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    counter = 0
    flag = 0
    if len(s) > 1 and s[0] == 'u' and s[1] == 'm':
        flag = 1
    for i, c in enumerate(s):
        #print(i)
        if i == len(s) - 1:
            break
        if c.isspace() and i < (len(s) - 2):
            if s[i+1] == 'u' and s[i+2] == 'm':
                flag = 1
        #print("1 is ok")
        if s[i] == 'u' and s[i+1] == 'm':
            #print("2 is ok")
            if i == len(s) - 2:
                #print("3 is ok")
                if flag == 1:
                    counter += 1
                    flag = 0 #just in case
            else:
                #print("else")
                #print(flag)
                if flag == 1 and i < len(s) - 2 and (s[i+2].isspace() or s[i+2] == ',' or s[i+2] == '.' or s[i+2] == '?' or s[i+2] == '!'):
                    #print("4 is ok")
                    counter += 1
                    flag = 0
    return counter


...


if __name__ == "__main__":
    main()
