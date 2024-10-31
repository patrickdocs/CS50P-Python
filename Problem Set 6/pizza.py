import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".csv"):
            sys.exit("Not a CSV file")
        print(draw_table(file_name))

def draw_table(file_name):
    try:
        with open(file_name,"r") as file:
            data = list(csv.reader(file))
            headers = data[0]
            table = data[1:]
            return tabulate(table, headers, tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exit")
if __name__ == "__main__":
    main()


