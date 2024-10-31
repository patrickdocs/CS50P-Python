def main():
    t = str(input("What time is it? "))
    u = convert(t)
    if 7 <= u <=8: print("breakfast time")
    elif 12 <= u <=13: print("lunch time")
    elif 18 <= u <=19: print("dinner time")

def convert(time):
    h,m = time.split(":")
    time = float(h)+float(m)/60
    return time

if __name__ == "__main__":
    main()
