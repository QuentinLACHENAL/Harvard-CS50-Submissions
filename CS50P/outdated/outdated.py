month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()
    if (date.find('/') != -1):
        #format MM/DD/YYYY
        date = date.split('/')
        if not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit():
            continue
        if (int(date[0]) > 12):
            continue
        if (int(date[1]) > 31):
            continue
        print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")
        break

    elif (date.find(',') != -1):
        #format Month Day, Year
        date = date.split(' ')
        if not date[0] in month:
            continue
        if not date[2].isdigit():
            continue
        date[1] = date[1].replace(',', '')
        if not date[1].isdigit():
            continue
        date[1] = int(date[1])
        if date[1] > 31:
            continue
        print(f"{date[2]}-{(month.index(date[0]) + 1):02}-{date[1]:02}")
        break

