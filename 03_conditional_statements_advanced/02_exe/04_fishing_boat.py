def fishing_boat(budget: int, season_of_year: str, n_fisher_mans: int):
    total = 0

    price = {
        'Spring': 3_000,
        'Summer': 4_200,
        'Autumn': 4_200,
        'Winter': 2_600,
    }

    total = price[season_of_year]

    if n_fisher_mans <= 6:
        total -= total * 0.10

    elif n_fisher_mans <= 11:
        total -= total * 0.15

    else:
        total -= total * 0.25

    if (n_fisher_mans % 2 == 0) and (not season_of_year == 'Autumn'):
        total -= total * 0.05

    diff = abs(budget - total)

    if budget >= total:
        return f'Yes! You have {diff:.2f} leva left.'

    return f'Not enough money! You need {diff:.2f} leva.'


budget = int(input())
season_of_year = input()
n_fisher_mans = int(input())
result = fishing_boat(budget, season_of_year, n_fisher_mans)

print(result)
