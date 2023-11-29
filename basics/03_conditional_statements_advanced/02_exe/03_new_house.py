type_flowers = input()
num_flowers = int(input())
budget = int(input())

rose = 5.00
dahlia = 3.80
tulip = 2.80
narcissus = 3.00
gladiolus = 2.50

total = 0

if type_flowers == 'Roses':
    if num_flowers > 80:
        total += (rose * num_flowers) - ((rose * num_flowers) * 0.10)
    else:
        total += rose * num_flowers

if type_flowers == 'Dahlias':
    if num_flowers > 90:
        total += (dahlia * num_flowers) - ((dahlia * num_flowers) * 0.15)

    else:
        total += dahlia * num_flowers

if type_flowers == 'Tulips':
    if num_flowers > 80:
        total += (tulip * num_flowers) - ((tulip * num_flowers) * 0.15)

    else:
        total += tulip * num_flowers

if type_flowers == 'Narcissus':
    if num_flowers < 120:
        total += (narcissus * num_flowers) * 1.15

    else:
        total += narcissus * num_flowers

if type_flowers == 'Gladiolus':
    if num_flowers < 80:
        total = (gladiolus * num_flowers) * 1.20

    else:
        total += gladiolus * num_flowers

diff = abs(budget - total)

if budget >= total:
    print(f'Hey, you have a great garden with {num_flowers} {type_flowers} and {diff:.2f} leva left.')

else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
