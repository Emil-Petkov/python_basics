budget = int(input())
season_of_year = input()
num_fishman = int(input())

total = 0

if season_of_year == 'Spring':
    total += 3_000

elif season_of_year in ['Summer', 'Autumn']:
    total += 4_200

elif season_of_year == 'Winter':
    total += 2_600

if num_fishman <= 6:
    total -= total * 0.10

elif 7 <= num_fishman <= 11:
    total -= total * 0.15

elif num_fishman > 12:
    total -= total * 0.25

if num_fishman % 2 == 0 and not season_of_year == 'Autumn':
    total -= total * 0.05

diff = abs(budget - total)

if budget >= total:
    print(f'Yes! You have {diff:.2f} leva left.')

else:
    print(f'Not enough money! You need {diff:.2f} leva.')
