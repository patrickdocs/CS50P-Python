import re
import sys

def main():
    try:
        print(convert(input("Hour: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(hour):
    pattern = r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$"
    match = re.search(pattern, hour)
    if not match:
        raise ValueError

    h1, m1, period1, h2, m2, period2 = match.groups()
    if m1: m1 = m1[1:]
    else: m1 = "00"
    if m2: m2 = m2[1:]
    else: m2 = "00"

    if not (0 <= int(h1) <= 12 and 0 <= int(h2) <= 12 and 0 <= int(m1) < 60 and 0 <= int(m2) < 60):
        raise ValueError
    start_time = to_24h_clock(int(h1), int(m1), period1)
    end_time = to_24h_clock(int(h2), int(m2), period2)

    return f"{start_time} to {end_time}"

def to_24h_clock(hour, minute, period):
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()





