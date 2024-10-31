import re

def main():
    print(count(input("Text: ")))

def count(s): #Count "um" in Text:
    um_pattern = r"\bum\b"
    return len(re.findall(um_pattern, s, re.IGNORECASE))

if __name__ == "__main__":
    main()
