greet = input("Greeting: ").upper().strip()
greet = greet[:5]

if greet == "HELLO":
    print("$0")
elif greet[0] == 'H':
    print("$20")
else:
    print("$100")
