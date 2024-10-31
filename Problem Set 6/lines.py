import sys

def count_lines(file_name):
    count = 0
    try:
        with open(file_name, "r") as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        if not file_name.endswith(".py"):
            sys.exit("Not a Python file")
        lines = count_lines(file_name)
        print(lines)

if __name__ == "__main__":
    main()
