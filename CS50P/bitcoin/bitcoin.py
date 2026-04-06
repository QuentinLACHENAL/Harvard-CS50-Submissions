import requests
import sys

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)
try:
    float(sys.argv[1])
except:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    req = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=791d9cdbef69f0d353690a8d6e7c4192f1db212e6454f3007bf1fb5244751ca5')
    amount = req.json()
    try:
        resp = float(amount["data"]["priceUsd"]) * float(sys.argv[1])
    except:
        print("Too large amount for float")
        sys.exit(0)
    print(f"${resp:,.4f}")

except requests.RequestException:
    sys.exit(1)
