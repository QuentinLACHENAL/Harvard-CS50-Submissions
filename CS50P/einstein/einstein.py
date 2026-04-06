def main():
    mass = int(input("m: "))
    mass = calculate(mass)
    print(f"E: {mass}")

def calculate(mass):
    return mass * 300000000 * 300000000

main()
