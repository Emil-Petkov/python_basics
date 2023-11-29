budget = float(input())
season_of_year = input()

total = 0
destination = ''
place = ''

if budget <= 100:
    destination = 'Bulgaria'

    if season_of_year == 'summer':
        total -= budget * 0.30
        place = 'Camp'

    elif season_of_year == 'winter':
        total -= budget * 0.70
        place = 'Hotel'

elif budget <= 1_000:
    destination = 'Balkans'

    if season_of_year == 'summer':
        total -= budget * 0.40
        place = 'Camp'

    elif season_of_year == 'winter':
        total -= budget * 0.80
        place = 'Hotel'

elif budget > 1_000:
    destination = 'Europe'

    total -= budget * 0.90
    place = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {abs(total):.2f}')
