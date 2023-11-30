budget = float(input())
season_of_year = input()

type_of_car = ''
class_of_car = ''

if season_of_year == 'Summer':
    type_of_car = 'Cabrio'

    if budget <= 100:
        class_of_car = 'Economy class'
        budget = budget * 0.35

    elif 100 < budget <= 500:
        class_of_car = 'Compact class'
        budget = budget * 0.45

if season_of_year == 'Winter':
    type_of_car = 'Jeep'

    if budget <= 100:
        class_of_car = 'Economy class'
        budget = budget * 0.65

    elif 100 < budget <= 500:
        class_of_car = 'Compact class'
        budget = budget * 0.80

if budget > 500:
    type_of_car = 'Jeep'
    class_of_car = 'Luxury class'
    budget = budget * 0.90

print(class_of_car)
print(f'{type_of_car} - {budget:.2f}')
