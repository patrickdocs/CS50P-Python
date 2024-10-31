import inflect

p = inflect.engine()
def main():
    names = []

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    farewell = p.join(names)
    print("Adieu, adieu, to",farewell)

if __name__ == "__main__":
    main()
