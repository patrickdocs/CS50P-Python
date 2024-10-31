import validators

def main():
    email = input("What's your email address? ")
    is_valid(email)

def is_valid(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/response

