def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6: return False
    if not s[0:2].isalpha(): return False

    num_started = False
    number = ""
    for i, char in enumerate(s):
        if not char.isalnum(): return False
        if char.isdigit():
            num_started = True
            number += char
            if number[0] == '0': return False
        elif num_started:
            return False  # Letters after numbers are invalid

    return True


if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/tests/plates
