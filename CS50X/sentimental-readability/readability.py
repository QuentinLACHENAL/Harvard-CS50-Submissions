from cs50 import get_string

text = get_string("Text: ")

letters = len(list(filter(str.isalpha, text)))
words = len(text.split())
sentences = text.count('.') + text.count('?') + text.count('!')

L = (letters / float(words)) * 100
S = (sentences / float(words)) * 100

index = round((0.0588 * L) - (0.296 * S) - 15.8)

if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
