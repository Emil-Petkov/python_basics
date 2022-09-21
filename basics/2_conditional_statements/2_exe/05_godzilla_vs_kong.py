budget = float(input())
count_statists = int(input())
cloths_price_per_one_statist = float(input())

decor = budget * 0.10
money_per_cloths = count_statists * cloths_price_per_one_statist

if count_statists > 150:
    money_per_cloths = money_per_cloths - (money_per_cloths * 0.10)

total = decor + money_per_cloths

diff = abs(total - budget)

if total <= budget:
    print(f'Action!\nWingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!\nWingard needs {diff:.2f} leva more.')
