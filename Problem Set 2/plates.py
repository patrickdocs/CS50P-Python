def main():
    plate = input("Plate: ")
    if is_valid(plate): print("Valid")
    else: print("Invalid")

def is_valid(s):
    x = ""
    if not s[0:2].isalpha(): return False
    if not 2 <= len(s) <= 6: return False
    if any(char in ' .,-' for char in s): return False

    for i in range(1,len(s)):
        if s[i].isalpha() and s[i-1].isdigit():
            return False
        if s[i].isdigit():
            x += s[i]
            if x[0] == "0": return False

    return True

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/plates
