calories = {
    "APPLE" : 130,
    "AVOCADO" : 50,
    "BANANA" : 110,
    "CANTALOUPE" : 50,
    "GRAPEFRUIT" : 60,
    "GRAPES" : 90,
    "HONEYDEW MELON" : 50,
    "KIWIFRUIT" : 90,
    "LEMON" : 15,
    "LIME" : 20,
    "NECTARINE" : 60,
    "ORANGE" : 80,
    "PEACH" : 60,
    "PEAR" : 100,
    "PINEAPPLE" : 50,
    "PLUMS" : 70,
    "STRAWBERRIES" : 50,
    "SWEET CHERRIES" : 100,
    "TANGERINE" : 50,
    "WATERMELON" : 80
}

def main():
    fruit = str(input("Items: ")).upper()
    if fruit in calories:
        print(calories.get(fruit))

if __name__ == "__main__":
    main()
