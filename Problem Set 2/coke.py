amount_due = 50
accept_coins = [5,10,25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accept_coins:
        amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
#check50 cs50/problems/2022/python/coke
