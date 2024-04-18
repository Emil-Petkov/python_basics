def godzilla_vs_kong(budget:float, n_statists:int, price_clothes_per_one_statist:float):
    decor = budget * 0.10
    money_for_clothes = n_statists * price_clothes_per_one_statist

    if n_statists > 150:
        money_for_clothes -= money_for_clothes * 0.10

    total_costs = decor + money_for_clothes

    diff = abs(budget - total_costs)

    if budget >= total_costs:
        return f'Action!\nWingard starts filming with {diff:.2f} leva left.'

    else:
        return f'Not enough money!\nWingard needs {diff:.2f} leva more.'


budget = float(input())
n_statists = int(input())
price_clothes_per_one_statist = float(input())
print(godzilla_vs_kong(budget, n_statists, price_clothes_per_one_statist))
