def dollars_to_float(d):
    return float(str(d).removeprefix("$"))

def percent_to_float(p):
    return float(str(p).removesuffix("%"))/100

def main():
    dollars = dollars_to_float(str(input("How much was the meal? ")))
    percent = percent_to_float(str(input("What percentage would you like to tip? ")))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

main()
#check50 cs50/problems/2022/python/tip
