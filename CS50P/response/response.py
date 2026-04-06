import sys
import validators
from validator_collection import validators, checkers, errors



def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        email_address = validators.email(s)

    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    return "Valid"

if __name__ == "__main__":
    main()
