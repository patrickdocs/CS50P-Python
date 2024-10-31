import random
def get_int():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                return random.randint(1, n)
            else: raise ValueError
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else: raise ValueError
        except ValueError:
            pass

def main():
    number = get_int()
    while True:
        guess = get_guess()
        if guess < number: print("Too small!")
        elif guess > number: print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()

