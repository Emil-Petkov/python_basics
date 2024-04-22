def journey(budget: float, season_of_year: str):
    current_budget = budget
    place = ''
    type = ''

    if budget <= 100:
        place = 'Bulgaria'

        if season_of_year == 'summer':
            type = 'Camp'
            current_budget -= budget * 0.30

        elif season_of_year == 'winter':
            type = 'Hotel'
            current_budget -= budget * 0.70

    elif budget <= 1_000:
        place = 'Balkans'

        if season_of_year == 'summer':
            type = 'Camp'
            current_budget -= budget * 0.40

        elif season_of_year == 'winter':
            type = 'Hotel'
            current_budget -= budget * 0.80

    else:
        place = 'Europe'
        type = 'Hotel'
        current_budget -= budget * 0.90

    costs = budget - current_budget

    return f'Somewhere in {place}\n{type} - {costs:.2f}'


budget = float(input())
season_of_year = input()
result = journey(budget, season_of_year)

print(result)
