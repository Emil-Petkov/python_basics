def journey(budget: float, season: str):
    place = ''
    type_vacation = ''
    total = 0

    if budget > 1000:
        type_vacation = 'Hotel'
        place = 'Europe'
        total = budget * 0.90

    elif budget <= 100:
        place = 'Bulgaria'

        if season == 'summer':
            type_vacation = 'Camp'
            total = budget * 0.30

        elif season == 'winter':
            type_vacation = 'Hotel'
            total = budget * 0.70


    else:
        place = 'Balkans'

        if season == 'summer':
            type_vacation = 'Camp'
            total = budget * 0.40

        elif season == 'winter':
            type_vacation = 'Hotel'
            total = budget * 0.80

    return place, type_vacation, total


budget = float(input())
seasons = input()

pla, vac, tot = journey(budget, seasons)
print(f'Somewhere in {pla}')
print(f'{vac} - {tot:.2f}')
