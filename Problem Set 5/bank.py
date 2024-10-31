def main():
    greeting = str(input())
    print(f"${value(greeting)}")

def value(greeting: str) -> int:
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else: return 100


if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/tests/bank

