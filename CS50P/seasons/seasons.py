import datetime
import inflect
import re
import sys

def main():
    return_txt(input("Date of Birth: "))

def return_txt(date):
    year, month, day = validate_date(date)

    now = datetime.date.today()
    birthtime = datetime.date(int(year), int(month), int(day))

    delta = now - birthtime

    p = inflect.engine()
    print((p.number_to_words(delta.days * 24 * 60, andword="") + " minutes").capitalize())

def validate_date(datetxt: str):
    try:
        year, month, day = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", datetxt).groups()
        datetime.date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid date")

    return year, month, day

if __name__ == "__main__":
    main()
