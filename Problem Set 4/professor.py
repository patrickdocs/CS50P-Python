import random

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

def main():
    level = get_level()
    score = 0

    for problem in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        for tries in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/professor
