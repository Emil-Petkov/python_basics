budget = float(input())
num_statists = int(input())
clothes_one_statist_price = float(input())

decor = budget * 0.10

money_for_clothes = num_statists * clothes_one_statist_price

if num_statists > 150:
    money_for_clothes -= money_for_clothes * 0.10

total_money_per_movie = money_for_clothes + decor

total = abs(budget - total_money_per_movie)

if budget >= total_money_per_movie:
    print('Action!')
    print(f'Wingard starts filming with {total:.2f} leva left.')

else:
    print(f'Not enough money!')
    print(f'Wingard needs {abs(total):.2f} leva more.')
