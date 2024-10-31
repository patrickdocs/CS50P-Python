def main():
    d = {}
    try:
        while True:
            item = input().strip().lower()
            if item in d:
                d[item] += 1
            else: d[item] = 1

    except (EOFError, KeyError):
        pass

    list = sorted(d.items())
    for item, count in list:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/grocery
