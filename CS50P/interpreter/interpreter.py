typed = input("Expression: ").split(' ')

x = int(typed[0])
y = typed[1]
z = int(typed[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print(f"{result:.1f}")
