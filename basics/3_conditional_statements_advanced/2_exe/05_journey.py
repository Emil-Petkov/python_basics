budget = float(input())
season = input()

costs = 0
destination = ''
place = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        costs = budget * 0.30
        place = 'Camp'
    elif season == 'winter':
        costs = budget * 0.70
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        costs = budget * 0.40
        place = 'Camp'
    elif season == 'winter':
        costs = budget * 0.80
        place = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    costs = budget * 0.90
    place = 'Hotel'

if budget >= costs:
    print(f'Somewhere in {destination}\n{place} - {costs:.2f}')
