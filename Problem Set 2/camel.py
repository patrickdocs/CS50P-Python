def snake_case(s):
    for i in range(len(s)):
        if s[i].isupper():
            s = s.replace(s[i],"_"+s[i].lower())
    return s

def main():
    camel = str(input("camelCase: "))
    snake = snake_case(camel)
    print(snake)

if __name__ == "__main__":
    main()

#check50 cs50/problems/2022/python/camel
