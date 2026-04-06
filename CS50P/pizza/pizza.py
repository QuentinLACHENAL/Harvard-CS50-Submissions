from tabulate import tabulate
import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not (len(sys.argv[1]) >= 3 and sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as menu:
        reader = csv.DictReader(menu)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")


