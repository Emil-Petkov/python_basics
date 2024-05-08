



money = float(input())

coins = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

counter = 0

while money > 0:
    for coin in coins:

        if money >= coin:
            count = int(money // coin)

            counter += count
            money -= count * coin
            money = round(money, 2)

print(counter)
