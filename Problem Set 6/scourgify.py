import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        file_input = sys.argv[1]
        file_output = sys.argv[2]
        convert(file_input,file_output)

def convert(file_input, file_output):
    try:
        with open(file_input, "r", newline='') as fi, \
            open(file_output, "w", newline='') as fo:
            reader = csv.DictReader(fi)
            writer = csv.writer(fo)


            writer.writerow(["first", "last", "house"])

            for row in reader:
                full_name = row['name'].split(", ")
                last_name = full_name[0]
                first_name = full_name[1]
                house = row['house']

                writer.writerow([first_name, last_name, house])

    except FileNotFoundError:
        sys.exit("File does not exist")
    except IOError:
        sys.exit("An I/O error occur")

if __name__ == "__main__":
    main()
