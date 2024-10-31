def main():
    word = str(input("Input: "))
    print(shorten(word))

def shorten(word):
    vowels = ["U", "E", "O", "A", "I", "u", "e", "o", "a", "i"]
    x = ""
    for i in range (0,len(word)):
        if word[i] not in vowels:
            x += word[i]
    return x

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/tests/twttr
