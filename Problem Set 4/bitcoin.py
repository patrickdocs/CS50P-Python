import requests
import sys

def get_price():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    return data['bpi']['USD']['rate_float']

def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        try:
            bitcoins = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    price = get_price()
    total = bitcoins * price

    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
