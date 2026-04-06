from random import randint
import sys

while True:
    try:
        n = int(input("Level: "))
        break
    except ValueError:
        continue

toGuess = randint(1, n)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < 1:
        continue
    if guess == toGuess:
        print("Just right!")
        sys.exit(0)
    elif guess < toGuess:
        print("Too small!")
    elif guess > toGuess:
        print("Too large!")
