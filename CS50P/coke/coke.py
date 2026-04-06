

price = 50

while (price > 0):
    print(f"Amount Due: {price}")
    coin = int(input("Insert Coin: "))
    if coin == 25:
        price -= coin
    elif coin == 10:
        price -= coin
    elif coin == 5:
        price -= coin

print(f"Change Owed: {price * -1}")
