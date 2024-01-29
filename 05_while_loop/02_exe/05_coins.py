















money = float(input())
change_in_cents = int(money * 100)

coins_values = [200, 100, 50, 20, 10, 5, 2, 1]

coins_count = 0
current_coin_index = 0

while change_in_cents > 0:
    coin = coins_values[current_coin_index]
    if change_in_cents >= coin:
        change_in_cents -= coin
        coins_count += 1
    else:
        current_coin_index += 1

print(coins_count)
