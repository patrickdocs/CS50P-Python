def main():
    while True:
        try:
            fraction = str(input()).strip()
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            break

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    percentage = round(x / y) * 100
    if x > y: raise ValueError
    if y == 0: raise ZeroDivisionError
    return percentage


def gauge(percentage):
    if percentage <= 1: return "E"
    elif percentage >= 99: return "F"
    else: return f"{percentage}%"


if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/tests/fuel
