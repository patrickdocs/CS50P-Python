vowels = ("a","e","i","o","u","A","E","I","O","U")
def main():
    s_input = str(input("Input: "))
    s_output = ""
    for i in range (len(s_input)):
        if s_input[i] not in vowels:
            s_output += s_input[i]
    print(s_output)

if __name__ == "__main__":
    main()

#check50 cs50/problems/2022/python/twttr
