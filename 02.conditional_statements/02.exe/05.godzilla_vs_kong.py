def godzilla_vs_kong(budget: float, n_statists: int, clothes_for_one_statist_price: float):
    price_for_clothes = n_statists * clothes_for_one_statist_price
    decor = budget * 0.10

    if n_statists > 150:
        price_for_clothes -= price_for_clothes * 0.10

    total = price_for_clothes + decor

    diff = abs(budget - total)
    if budget >= total:
        print('Action!')
        print(f'Wingard starts filming with {diff:.2f} leva left.')
    else:
        print('Not enough money!')
        print(f'Wingard needs {diff:.2f} leva more.')


budget = float(input())
n_statists = int(input())
clothes_for_one_statist_price = float(input())

godzilla_vs_kong(budget, n_statists, clothes_for_one_statist_price)
