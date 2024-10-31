months = [
    "January",    "February",    "March",    "April",    "May",    "June",
    "July",    "August",    "September",    "October",    "November",    "December" ]

def main():
    while True:
        try:
            date = str(input("Date: ")).strip()
            output_date = convert(date)
            if output_date:
                print(output_date)
                break
            else: pass
        except TypeError:
            pass


def convert(date):
    if "/" in date:
        month, day, year = date.split("/")
        if month.isdigit() and day.isdigit() and year.isdigit():
            month, day, year = int(month), int(day), int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year:04}-{month:02}-{day:02}"

    elif "," in date:
        md, year = date.split(",")
        year = int(year.strip())
        m, day = md.split()
        if m in months and day.isdigit():
            month = months.index(m) + 1
            day = int(day)
            if 1 <= day <= 31:
                return f"{year:04}-{month:02}-{day:02}"

    else:
        return None


if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/outdated
