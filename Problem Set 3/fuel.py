def get_int():
    while True:
        try:
            fraction = str(input("Fraction: "))
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if x <= y:
                return x / y * 100
            else:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            pass

def main():
    fuel = get_int()
    if fuel <= 1: print("E")
    elif fuel >= 99: print("F")
    else:
        print(f"{fuel:.0f}%")

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/fuel

