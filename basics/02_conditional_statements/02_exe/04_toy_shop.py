trip_price = float(input())

nums_puzzles = int(input())
nums_dolls = int(input())
nums_teddy_bear = int(input())
nums_minions = int(input())
nums_trucks = int(input())

puzzle_price = 2.60
doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

num_toys = nums_puzzles + nums_dolls + nums_teddy_bear + nums_minions + nums_trucks

sum_for_toys = ((nums_puzzles * puzzle_price) + (nums_dolls * doll_price) +
                (nums_teddy_bear * teddy_bear_price) + (nums_minions * minion_price) +
                (nums_trucks * truck_price))

if num_toys >= 50:
    sum_for_toys -= sum_for_toys * 0.25

rent = sum_for_toys * 0.10

total = sum_for_toys - rent

if total >= trip_price:
    diff = total - trip_price
    print(f'Yes! {diff:.2f} lv left.')

else:
    diff = total - trip_price
    print(f'Not enough money! {abs(diff):.2f} lv needed.')
