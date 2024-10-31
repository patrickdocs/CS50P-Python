import re
import sys

def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")
        sys.exit(1)  

def validate(ip):
    # Regular expression to match a valid IPv4 address
    pattern = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

    match = re.search(pattern, ip)

    if match:
        parts = match.groups()
        for part in parts:
            # Convert to an integer and check if it's between 0 and 255
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
