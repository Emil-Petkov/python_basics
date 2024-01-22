def fishing_boat(budget, season_of_year, n_fisherman):
    total = 0

    # season of the year
    if season_of_year == 'Spring':
        total += 3_000

    elif season_of_year in ['Summer', 'Autumn']:
        total += 4_200

    elif season_of_year == 'Winter':
        total += 2_600

    if n_fisherman <= 6:
        total -= total * 0.10

    elif n_fisherman <= 11:
        total -= total * 0.15

    elif n_fisherman > 12:
        total -= total * 0.25

    if n_fisherman % 2 == 0 and not season_of_year == 'Autumn':
        total -= total * 0.05

    diff = abs(budget - total)
    if budget >= total:
        return f'Yes! You have {diff:.2f} leva left.'

    else:
        return f'Not enough money! You need {diff:.2f} leva.'


budget = int(input())
season_of_year = input()
n_fisherman = int(input())
print(fishing_boat(budget, season_of_year, n_fisherman))
