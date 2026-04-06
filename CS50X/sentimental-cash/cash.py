from cs50 import get_float

cash = -1
while cash < 0:
    cash = get_float("Change: ")

quarters = 0
dimes = 0
nickels = 0
pennies = 0

while round(cash, 2) >= 0.25:
    cash -= 0.25
    quarters += 1
while round(cash, 2) >= 0.10:
    cash -= 0.10
    dimes += 1
while round(cash, 2) >= 0.05:
    cash -= 0.05
    nickels += 1
while round(cash, 2) >= 0.01:
    cash -= 0.01
    pennies += 1

total = quarters + dimes + nickels + pennies
print(f"{total}")
