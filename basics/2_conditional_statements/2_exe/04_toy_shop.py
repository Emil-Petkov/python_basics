trip_price = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

price_per_puzzle = 2.60
price_per_doll = 3.00
price_per_teddy_bear = 4.10
price_per_minion = 8.20
price_per_truck = 2.00

discount = 0

sum = count_puzzles * price_per_puzzle + count_dolls * price_per_doll + count_teddy_bears * price_per_teddy_bear \
      + count_minions * price_per_minion + count_trucks * price_per_truck

quantity = count_puzzles + count_dolls + count_teddy_bears + count_minions + count_trucks

if quantity >= 50:
    discount = sum * 0.25

rent = (sum - discount) * 0.10

profit = sum - discount - rent

difference = abs(profit - trip_price)

if profit >= trip_price:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')
