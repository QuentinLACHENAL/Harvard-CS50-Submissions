import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not (len(sys.argv[1]) >= 5 and sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")

if not (len(sys.argv[2]) >= 5 and sys.argv[1].endswith(".csv")):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], 'r') as csv1:
        reader1 = csv.DictReader(csv1)
        fieldnames = ["first", "last", "house"]
        with open(sys.argv[2], 'w') as csv2:
            writer = csv.DictWriter(csv2, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader1:
                splitted = row['name'].split(", ")
                writer.writerow(
                    {
                        "first": splitted[1],
                        "last": splitted[0],
                        "house": row['house']
                    }
                )
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


#with open('after.csv', 'w') as csv2:
#    writer = csv.writer(csv2)
 #   writer.writerows(newDict)

