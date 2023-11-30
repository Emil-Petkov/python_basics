budget = float(input())
season_of_year = input()

location = ''
accommodation = ''

if season_of_year == 'Summer':
    if budget <= 1_000:
        location = 'Alaska'
        accommodation = 'Camp'
        budget *= 0.65

    elif 1_000 < budget <= 3_000:
        location = 'Alaska'
        budget *= 0.80
        accommodation = 'Hut'

    elif budget > 3_000:
        location = 'Alaska'
        budget *= 0.90
        accommodation = 'Hotel'


elif season_of_year == 'Winter':
    if budget <= 1_000:
        location = 'Morocco'
        accommodation = 'Camp'
        budget *= 0.45

    elif 1_000 < budget <= 3_000:
        location = 'Morocco'
        budget *= 0.60
        accommodation = 'Hut'

    elif budget > 3_000:
        location = 'Morocco'
        budget *= 0.90
        accommodation = 'Hotel'

print(f'{location} - {accommodation} - {budget:.2f}')
